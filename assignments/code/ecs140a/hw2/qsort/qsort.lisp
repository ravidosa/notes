(defun lt (n xs)
  (cond
    ((null xs)
      nil
    )
    ((< (car xs) n)
      (cons (car xs) (lt n (cdr xs)))
    )
    (t
      (lt n (cdr xs))
    )
  )
)

(defun geq (n xs)
  (cond
    ((null xs)
      nil
    )
    ((>= (car xs) n)
      (cons (car xs) (geq n (cdr xs)))
    )
    (t
      (geq n (cdr xs))
    )
  )
)

(defun pivot (n xs)
  (list (lt n xs) (geq n xs))
)

(defun quicksort (xs)
  (cond
    ((null xs)
      nil
    )
    (t
      (let ((pivoted (pivot (car xs) xs)))
        (append (quicksort (car pivoted)) (list (car xs)) (quicksort (cdr (car (cdr pivoted)))))
      )
    )
  )
)
