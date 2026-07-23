# Contiki-NG MARTHR OCP scaffold

This note documents a minimal Objective Function (OCP) adapter for Contiki-NG / rpl-lite.

## Intended role
The file `marthr_ocp.c` provides a lightweight rank computation hook that can be wired into a Contiki RPL objective function.

## Integration sketch
1. Include the MARTHR context and score helpers.
2. Compute a context-aware weight vector from trust, threat, and energy state.
3. Return a rank that favors trustworthy and energy-sustainable parents.
4. Plug the resulting function into the OCP selection logic used by rpl-lite.
