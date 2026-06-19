# Fourier Transform–Based Instance Decomposition of the Quadratic Assignment Problem 🧩

This repository provides an efficient implementation of the Fourier transform (FT)–based instance decomposition of Quadratic Assignment Problem (QAP) instances. Given a QAP instance in QAPLIB format (https://qaplib.mgi.polymtl.ca/), the software generates four sub-instances corresponding to the individual Fourier components of the original objective function:

* **n.dat** — Contains the contribution associated with the **(n)** irreducible representation.
* **n_1_1.dat** — Contains the contribution associated with the **(n−1,1)** irreducible representation.
* **n_2_2.dat** — Contains the contribution associated with the **(n−2,2)** irreducible representation.
* **n_2_1_1.dat** — Contains the contribution associated with the **(n−2,1,1)** irreducible representation.

Each generated sub-instance has the same dimension as the original QAP instance. In all cases, the distance matrix remains unchanged, so only the flow matrix is modified to reflect the contribution of the corresponding Fourier component.

To apply the decomposition, just execute:

`python3 main.py`

and follow the instructions.

## Dependencies ⚙️

The software has been tested with

* Python 3.12.2
  * numpy 2.3.4
