(defun vector-dot (vec1 vec2)
  (cond
    ((and (null vec1) (null vec2))
      0
    )
    (t
      (+ (* (car vec1) (car vec2)) (vector-dot (cdr vec1) (cdr vec2)))
    )
  )
)

(defun vector-matrix-multiply (vec mat)
  (mapcar #'(lambda (col) (vector-dot vec col)) (matrix-transpose mat))
)

(defun matrix-add (mat1 mat2)
  (mapcar (lambda (row1 row2) (mapcar #'+ row1 row2)) mat1 mat2)
)

(defun matrix-transpose (mat)
  (apply #'mapcar #'list mat)
)

(defun matrix-multiply (mat1 mat2)
  (mapcar #'(lambda (row) (vector-matrix-multiply row mat2)) mat1)
)

