(defun say-hello()
  (prin1 "Enter your Name: ")
  (setf name (read))
  (print name))


(defun own-repl()
  (loop (print(eval(read)))))


(defun game-repl()
  (let ((cmd (game-read)))))

(defun game-read()
  (let ((read-contents
         (read-from-string (concatenate 'string "(" (read-line) ")"))))
    (append (list (car read-contents))
          (mapcar (lambda(x)(quote (x)) (cdr read-contents))
    )
  )))
