## OCaml Notes

### Run and Compile OCaml Code

#### **Method 1 – Manual compile**

```bash
ocamlc -o filename.byte filename.ml
./filename.byte
```

#### **Method 2 – Using Dune**

```bash
# create project file
echo "(lang dune 3.4)" > dune-project

# create build file
echo "(executable (name filename))" > dune

# build, run, clean
dune build
dune exec ./filename.exe
dune clean
```

---

```ocaml
print_endline "Hello, World!";;  (* prints and adds a newline. *)

print_string "Hello, World!";;  (* prints without adding a newline. *)

"Functional " ^ "Programming";; (* string concatenation *)

if 5 < 10 then "Correct" else "Incorrect";;

let x = 15;;
let y = 5;;
x + y;;
(* 20 *)

(fun x y -> (x +. y) /. 2.);; (* anonymous function for average of two floats *)
```
