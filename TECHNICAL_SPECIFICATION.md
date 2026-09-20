# **Technical specification - Sluier**


#### Project name: Sluier
#### Version: 1.0
#### Language: Python 3.13
#### Interface language: English

---

## 1. Project Overview

Sluier is an interactive Python application designed to demonstrate the mathematical principles behind modern cryptographic algorithms and provide practical cryptographic operation using the _cryptography_ library.

The application is divided into two main modes:

* Educational Mode - demonstrates how cryptographic algorithms works internally using custom educational implementations.
* Practical Mode - provides practical cryptographic operations using established implementations from the Python _cryptography_ library.

The educational implementations are intended for learning purposes only and should not be used to protect real-world sensitive information.

---

## 2. Project Objectives

The main objectives of the project are:

* to demonstrate the mathematics principles behind public-key cryptography.
* to provide an interactive way to explore RSA and elliptic-curve cryptography.
* to demonstrate key generation, encryption, decryption, key exchange and digital signatures.
* to compare educational implementations with established cryptographic libraries.
* to demonstrate how cryptographic primitives are used in practical software.
* to provide a clear and user-friendly graphical interface.

---

## 3. Target Audience

The application is intended for:

* students learning cryptography;
* beginner programmers;
* students interested in cybersecurity;
* users who want to understand how RSA and ECC work;
* developers learning how to use Python cryptographics libraries.

---

## 4. Applications Modes

### 4.1 Educational Mode

Educational Mode is designed to explain the mathematics principles of cryptography.

The application should use custom implementations for educational algorithms rather than relying on corresponding high-level cryptographic operations provided by external libraries.

The mode should provide:

* step-by-step calculations;
* intermediate results;
* mathematics explanations;
* visualization where appropriate;
* small parameters suitable for demonstration.

The application should clearly display a warning:
_Educational implementation - not intended for protecting real data._

### 4.2 Practical Mode

Practical Mode is designed for performing real cryptographic operations using Python _cryptography_ library.

The applications should provide:

* secure key generation;
* encryption and decryption;
* digital signatures;

Where appropriate, the application should use established high-level cryptographic construction.

Lower-level cryptographic primitives might be exposed thought an **Advanced** interface for educational or technical exploration.

---

## 5. Educational Mode Requirements

### 5.1 RSA

The application should provide an interactive RSA demonstration.

The user should be able to:

* enter or generate suitable prime numbers _p_ and _q_;
* calculate _n_;
* calculate Euler's totient function;
* select a valid public exponent _e_;
* calculate a private exponent _d_;
* enter a numerical message;
* encrypt the message;
* decrypt the message;
* view intermediate calculations;

For educational purposes, the application might use small numbers.

### 5.2 ECC Point

The application should provide an interactive explorer for elliptic-curve arithmetic.

The user should be able to specify:

* prime modulus _p_;
* curve parameters _n_ and _r_;
* a point _G_;

The application should support:

* point validation;
* point addition;
* point doubling;
* scalar multiplication;
* calculation of _nG_;
* displaying intermediate calculations;

### 5.3 ECDH Demonstration

The application should provide an educational demonstration of Elliptic Curve Diffie-Hellman.

The application should demonstrate, that both participants independently derive the same shared secret.

---

## 6. Practical Mode Requirements

### 6.1 RSA

The application should support:

* RSA key generation;
* configurable key size where appropriate;
* RSA-OAEP encryption;
* RSA-OAEP decryption;

The implementation should use the _cryptography_ library rather than educational RSA implementational.

### 6.2 AES-GCM

The application should provide authenticated symmetric encryption using AES-GCM.

The user should be able to:

* generate a key;
* encrypt a message;
* decrypt a message;
* generate a secure key;
* display the resulting _ciphertext_;

The application should correctly handle authentication failures and invalid ciphertext.

### 6.3 Digital Signatures

The application should provide digital signature functionality.

At minimum, it should support:

* message signing;
* signature verification;
* detection of modified messages;

### 6.4 Implementation Levels

Practical Mode should distinguish between recommended cryptographic constructions and advanced primitives.

**Recommended**

The application should use established, ready-to-use constructions provided by the _cryptography_ library.

The user should not need to configure lower-level cryptographic parameters unless necessary.

**Advanced**

An optional Advanced interface might expose lower-level cryptographic primitives.

This selection is intended for technically experienced users and educational exploration.

---

## 7. User Interface Requirements

The entire user interface should be in English.

The Interface should:

* provide clear input fields;
* display meaningful error message;
* clearly distinguish educational and practical functionality;
* display security warning where appropriate;

---

## 8. Error Handling

The application should handle invalid data without crashing.

The following cases should be handled:

* invalid numbers;
* invalid prime numbers;
* invalid elliptic-curve points;
* points not belonging to the selected curve;
* invalid keys;
* invalid ciphertext;
* invalid signatures;
* invalid message format;
* empty input field;
* unsupposed parameters;

Error messages should explain the problem in the user-friendly way.

---

## 9. Security Requirements 

The project should follow these principles:

* Educational cryptographic implementational should not be presented as secure production cryptography.
* Practical cryptographic operation should use established cryptographic libraries.
* Modern cryptographic algorithms and recommended parameters should be preferred.
* Private keys and sensitive information should not be stored.

---

## 10.Testing requirements

The project should include automated tests.

Testing should cover both educational and practical implementations.

**RSA**

Tests should verify:

* keys generation;
* encryption/decryption correctness;
* invalid input handling;

**ECC**

Tests should verify:

* points validation;
* points addition;
* points doubling;
* scalar multiplication;
* known mathematical results;

**ECDH**

Tests should verify:

_First Shared Secret = Second Shared Secret_

**AES-GCM**

Tests should verify:

* successful encryption/decryption;
* modified ciphertext detection;
* invalid key handling;

**Digital Signatures**

* successful signature verification;
* detection of modified messages;
* detection of invalid signatures;

---

## 11. Project Structure

---

## 12. Technical Requirements

Programming language: **Python 3.13**

Cryptographic library: **cryptography**

Testing framework: **Pytest**

Version control: **Git/GitHub**

User interface: **PyQT6**

---

## 13. Documentation Requirements

The project should contain English README.md.

README should include:

* project description;
* project objectives;
* usage instruction;
* explanation of Education Mode;
* explanation of Practical Mode;

Additional technical documentation might be provided in the docs/ directory.

---

## 14. Out Of Scope

The following are outside the scope of the project:

* creating the production-ready cryptographic library;
* replacing established cryptographic libraries;
* implementing every existing cryptographic algorithm;
* creating a proprietary cryptographic protocol;
* providing guarantees of security equivalent to professionally audited cryptographic software;

---

## 15. Definition Of Done

The project will be considered complete when:

1. [ ] The main menu is implemented;
2. [ ] Educational Mode is functional:
   1. [ ] RSA educational demonstrated is implemented;
   2. [ ] ECC educational demonstrated is implemented;
   3. [ ] ECDH educational demonstrated is implemented;
3. [ ] Practical Mode is functional:
   1. [ ] Practical RSA is implemented using _cryptography_;
   2. [ ] AES-GCM is implemented;
   3. [ ] ECC/ECDH is implemented;
   4. [ ] Digital signatures are implemented;
4. [ ] Input validation is implemented;
5. [ ] Error handling is implemented;
6. [ ] Automated tests are implemented and passed;
7. [ ] Documentation is written in English;
8. [ ] The project can be installed and launched from a clean environment;

---