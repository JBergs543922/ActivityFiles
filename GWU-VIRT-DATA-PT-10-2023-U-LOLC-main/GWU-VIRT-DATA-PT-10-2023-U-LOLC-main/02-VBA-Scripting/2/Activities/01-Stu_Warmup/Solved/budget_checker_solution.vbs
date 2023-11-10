' Part I: Calculate the total after fees
' Part II: Create an alert if the item is above budget after fees.
' Part III: If the item is above budget, correct the price such that it would be "under budget"

' ----------------------------------------------------

Sub BudgetChecker()

    ' Part I
    ' ----------------------------------------------------

    ' 1. Retrieve the Price and Fees from the cells
    Dim total As Double
    Dim price As Double
    Dim fees As Double
    Dim budget As Double

    price = Range("F3").Value
    fees = Range("H3").Value
    budget = Range("B3").Value
    
    ' 2. Use these values to calculate the total
    total = price * (1 + fees)
    ' msgbox(total)

    ' 3. Enter the total into the appropriate cell
    Range("L3").Value = total

    ' Part II
    ' ----------------------------------------------------
    ' 5. Compare using conditionals whether total is greater than or less than the budget
    If budget > total Then

        MsgBox ("Under budget")

    Else

        MsgBox ("Over budget")

        ' Part III
        ' ----------------------------------------------------
        Dim newPrice As Double

        newPrice = budget / (1 + fees)

        'Use a worksheet function to round the new price down to the nearest whole dollar
        'newPrice = Application.WorksheetFunction.RoundDown(newPrice, 0)

        ' Change the price
        Range("F3").Value = newPrice

        ' Change the new total
        Range("L3").Value = newPrice * (1 + fees)

    End If


End Sub
