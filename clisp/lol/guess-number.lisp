;;; Guessing game


(defparameter *small* 1)
(defparameter *big* 100)

(defun guess-number()
    (ash (+ *small* *big*) -1)
)

(defun smaller()
     (setf *big* (- (guess-number) 1))
     (guess-number)

)
(defun bigger()
     (setf *small* (+ (guess-number) 1))
     (guess-number)
)
(defun start-over()
    (setf *small* 1)
    (setf *big* 100)
    (guess-number)
)

;; Trying out nested functions
(defun trial(n)
    (let
        (
            (temp1 100)
            (temp2 200)
        )
        (labels(
                    (println(s)
                         (print s)
                    )
                    (display_contents()
                        (println temp1)
                        (println temp2)
                        (println n)
                        (- 20 n)
                    )
            )
            (display_contents)
        )
    )
)
