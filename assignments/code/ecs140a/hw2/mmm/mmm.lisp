; You may define helper functions here
(defun min_ (xs)
    (cond
        ((null xs)
            nil
        )
        ((null (cdr xs))
            (car xs)
        )
        (t
            (let ((min_cdr (min_ (cdr xs))))
                (cond
                    ((< (car xs) min_cdr)
                        (car xs)
                    )
                    (t
                        min_cdr
                    )
                )
            )
        )
    )
)

(defun max_ (xs)
    (cond
        ((null xs)
            nil
        )
        ((null (cdr xs))
            (car xs)
        )
        (t
            (let ((max_cdr (max_ (cdr xs))))
                (cond
                    ((> (car xs) max_cdr)
                        (car xs)
                    )
                    (t
                        max_cdr
                    )
                )
            )
        )
    )
)

(defun sum_ (xs)
    (cond
        ((null xs)
            0
        )
        (t
            (+ (car xs) (sum_ (cdr xs)))
        )
    )
)

(defun length_ (xs)
    (cond
        ((null xs)
            0
        )
        (t
            (+ 1 (length_ (cdr xs)))
        )
    )
)

(defun min-mean-max (xs)
    (list (min_ xs) (/ (sum_ xs) (length_ xs)) (max_ xs))
)
