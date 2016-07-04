(defparameter *nodes*
    '(
        (living-room (you are in the living-room.
            a wizard is snoring loudly on the couch.))
        (garden (you are in a beautiful garden.
            there is a well in front of you.))
        (attic (you are in the attic.
            there is a giant welding torch in the corner.))
    )
)

(defparameter *edges* 
    '(
        (living-room (garden west door)
            (attic upstairs ladder))
        (garden (living-room east door))
        (attic (living-room downstairs ladder))
    )
)

;; Listing all visible objects and their locations
(defparameter *objects* '(whiskey bucket frog chain))
(defparameter *object-locations '(
    (whiskey living-room)
    (bucket living-room)
    (frog garden)
    (chain garden)
))

;; Taking a look around
(defparameter *location* 'living-room)

;; User inventory
(defparameter *user-inventory* nil)

;; Method for getting the correct description
(defun describe-location(location container)
    ;; This is setting a global value.
    ;; This is not right. Use (let (())) from next
    ;; time. That's used for local instantiation.
    (defparameter location-value nil)
    (setf location-value (assoc location container))
    (cadr location-value)
    ;; This could also be simply done as 
    ;; (cadr (assoc location container))
)

(defun describe-path-from(from to container)
    (cdr (assoc to (cdr (assoc from container)))))

(defun describe-path (edge)
    `(there is a ,(caddr edge) going ,(cadr edge) from here.))

(defun describe-all-paths (location container)
    (apply #'append 
        (mapcar 
            #'describe-path 
            (cdr (assoc location container))
        )
    )
)

(defun objects-at(loc obj obj-loc)
    (labels 
        (
            (check-at-loc-p(o)
                (eq loc (cadr o))
            )
        )
        (
            mapcar
            #'car
            (remove-if-not 
                #'check-at-loc-p
                obj-loc
            )
        )
    )
)

(defun describe-objects (location obj obj-loc)
    (labels (
            (describe-object(o)
                `(you see a ,o on the floor.))
        )
        (apply #'append 
        (mapcar
            #'describe-object
            (objects-at location obj obj-loc)
        )
        )
    )
)

(defun look()
    (append 
        (describe-location *location* *nodes*)
        (describe-all-paths *location* *edges*)
        (describe-objects *location* *objects* *object-locations)
        ))

;; Moving it
(defun walk (dirn)
    ;; Check edges for dirn in current location
    (let (
            (next
                (find
                    dirn
                    (cdr (assoc *location* *edges*))
                    :key #'cadr   
                ) 
            )
        )
        (cond
            (next
                    (setf *location* (car next))
                    (look)
            )
            (t `(Wrong direction))
        )
    )
)

;; Picking things up
(defun pickup-stuff(obj)
    ;; Check if the object exists in the current location
    ;; Then remove the things and put it in the inventory
        (if (find obj *objects*)
            (progn
                (cond
                    ((eq (cadr (assoc obj *object-locations)) *location*)
                            (if (not (find obj *user-inventory*))
                                (setf *user-inventory* (append *user-inventory* (list obj)))
                                *user-inventory*
                                )
                        )
                    (t '(Such an object is not available in the room))
                    )
                
            )
            '(Such an object does not exist)
        )
    )

;; Checking inventory
(defun check-inventory()
    (append '(items-) *user-inventory*))