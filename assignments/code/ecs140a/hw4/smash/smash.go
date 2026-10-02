package smash

import (
	"io"
	"strings"
	"sync"
)

type word string

func Smash(r io.Reader, smasher func(word) uint32) map[uint32]uint {
	data, _ := io.ReadAll(r)

	words := strings.Fields(string(data))
	res := make(chan uint32, len(words))

	var wg sync.WaitGroup
	for _, w := range words {
		wg.Add(1)
		go func(wo string) {
			defer wg.Done()
			res <- smasher(word(wo))
		}(w)
	}
	go func() {
		wg.Wait()
		close(res)
	}()

	m := make(map[uint32]uint)
	for w := range res {
		m[w]++
	}
	return m
}
