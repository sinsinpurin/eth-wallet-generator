# Ethereum Wallet Generator

This is Ethereum wallet generator.
You can generate 1~100 Ethereum wallet.

[Generate]
- private key
- public key
- Ethereum Address(no format)
- Ethereum Address(format EIP-55)

You can output console, .txt, .xlsx.
.txt and .xlsx output in wallet directory.

(!) If you generate file again, already created file will be overwrite.
## setup

```
$> python setup.py install
```

## generate wallet

```
$> ethwalgen
```

## use packages
- coincurve             13.0.0     MIT or Apache-2.0
- inquirer              2.7.0      MIT
- openpyxl              3.0.3      MIT 
- pyfiglet              0.8.post1  MIT 
- pysha3                1.0.2      PSFL