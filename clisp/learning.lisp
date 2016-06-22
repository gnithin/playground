;;; The methods are from this tutorial - 
;;; http://www.cs.sfu.ca/CourseCentral/310/pwfong/Lisp/1/tutorial1.html

;; Triple a number
(defun triple(num)
    (* 3 num)
)

;; Finding the factorial
(defun factorial(n)
    (if (= n 1)
        1
        (* n (factorial (- n 1)))
    )
)

(defun fact_clone(n)
    (if (= n 1)
        1
        (+ n (fact_clone(- n 1)))
    )
)

;; Finding the power e^x
(defun power(e x)
    (if (= x 0)
        1
        (if (< x 0)
            "Value of exponent must be greater than 0"
            (if (= x 1)
                e
                (* e (power e (- x 1)))
            )
        )
    )
)

;; Figuring out the Exponent of the Binomial Expression
(defun B(n r)
    (if (> r n)
        "r > n. This is not a valid Binomial Expression."
        (if (or (zerop r) (= r n))
            1
            (+ 
                (B (- n 1) (- r 1)) 
                (B (- n 1) r)
            )
        )
    )
)

(defun B+(n r)
    (if (> r n)
        "r > n. This is not a valid Binomial Expression."
        (if (or (zerop r) (= r n))
            1
            (let
                (
                    (n1 (- n 1))
                )
                (+
                    (B n1 (- r 1))
                    (B n1 r)
                )
            )
        )
    )
)

;; Find the length of the list
(defun li_find_len(l)
    (if (null l)
        0   
        (+ 1 (get_len (rest l)))
    )
)


;; Find the sum of all the elements in the list
(defun li_find_sum(l)
    (if (null l)
        0
        (+ 
            (first l)
            (li_find_sum (rest l))
        )
    )
)


;; Find the nth element
;; Logic: pop every element, decrement index. Keep doing that till index is 0. Then remove the first element.
;; Check for bounds at the start.
(defun li_find_nth(n l)
    (if (or (null l) (null n) (< (list-length l) n))
        nil
        (if (= n 0)
            (first l)
            (li_find_nth (- n 1) (rest l))
        )
    )
)

;; Find the last element
(defun li_find_last(l)
    (if (null l)
        nil
        (if (null (rest l))
            ; Doesn't work
            ; '(first l)
            (cons (first l) nil)
            (li_find_last (rest l))
        )
    )
)

;; Implementing member
;; Implement this for all kinds for equality - list, symbols, chars et al.
;; http://stackoverflow.com/questions/547436/whats-the-difference-between-eq-eql-equal-and-equalp-in-common-lisp
(defun li_find_member(key l)
    (if (eq (first l) key)
        l
        (li_find_member key (rest l))
    )
)




































