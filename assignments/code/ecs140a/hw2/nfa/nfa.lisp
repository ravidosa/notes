(defun helper (transition next final input)
    (cond
        ((null next)
            nil
        )
        ((reachable transition (car next) final input)
            t
        )
        (t
            (helper transition (cdr next) final input)
        )
    )
)

(defun reachable (transition start final input)
    (cond
        ((null input)
            (eql start final)
        )
        (t
            (helper transition (funcall transition start (car input)) final (cdr input))
        )
    )
)
