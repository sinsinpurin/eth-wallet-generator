def outputConsole(wallet):
    print("+--------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| private-key    :" + wallet["privateKey"] +
          "                                                                 |")
    print("| public-key     :" + wallet["publicKey"] + " |")
    print("| address        :" +
          wallet["address"] + "                                                                                         |")
    print("| address(EIP-55):" + wallet["address(EIP-55)"] +
          "                                                                                         |")
    print("+--------------------------------------------------------------------------------------------------------------------------------------------------+\n")


def outputText(wallet, file):
    file.write("+--------------------------------------------------------------------------------------------------------------------------------------------------+\n")
    file.write("| private-key    :" + wallet["privateKey"] +
               "                                                                 |\n")
    file.write("| public-key     :" + wallet["publicKey"]+" |\n")
    file.write("| address        :" +
               wallet["address"]+"                                                                                         |\n")
    file.write("| address(EIP-55):" + wallet["address(EIP-55)"] +
               "                                                                                         |\n")
    file.write("+--------------------------------------------------------------------------------------------------------------------------------------------------+\n\n")


def outputXlsx(wallet, sheet, num):
    sheet.cell(row=num, column=1, value=num-1)
    sheet.cell(row=num, column=2, value=wallet["privateKey"])
    sheet.cell(row=num, column=3, value=wallet["publicKey"])
    sheet.cell(row=num, column=4, value=wallet["address"])
    sheet.cell(row=num, column=5, value=wallet["address(EIP-55)"])
