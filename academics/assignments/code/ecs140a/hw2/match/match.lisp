; You may define helper functions here

(defun match (pattern assertion)
  (cond
    ((and (null pattern) (null assertion))
      t
    )
    ((or (null pattern) (null assertion))
      nil
    )
    ((eq (car pattern) '!)
      (or
        (match (cdr pattern) (cdr assertion))
        (and (not (null assertion)) (match pattern (cdr assertion)))
      )
    )
    ((eq (car pattern) '?)
      (match (cdr pattern) (cdr assertion))
    )
    ((eq (car pattern) (car assertion))
      (match (cdr pattern) (cdr assertion))
    )
    (t
      nil
    )
  )
)
