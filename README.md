# A calculator interpreter.

## What it can do:
   `evaluate("(1+2)")` return `3`

   `evaluate("((((2*( 3 - 0 ))+ 15)/3)*4)")` return `28`

   Support following grammar:
   ```
       E->n
       E->(E OP E)
       OP-> one of +, -, *, /
   ```

## Misc
   The calculator includes:
   * a syntax parser (str2ast() function)
   * an evaluator (evaluate() function)

   and some tests.
