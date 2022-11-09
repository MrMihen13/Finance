# Project docs

The project includes the main aaps

* [income](#income)
* [cost app](#cost-app)
* [cauth](#cauth)

-------------------------------------------------------------------------

## Income

Income Tracking App

Tracks the amount of income, allows you to divide income into categories and offers the amount to replenish the reserve account, depending on the percentage selected for the user to replenish the reserve account.

### Basic entities:

#### FinancialIncomeCategory
- name: Char (Name of category)

-------------------------------------------------------------------------

#### FinancialIncome
- user: Foreing Key to [Customuser](#customuser)
- category: Foreing Key to [FinancialIncomeCategory](#financialincomecategory)
- income: PositiveInteger
- net_income: PositiveIntegerField

-------------------------------------------------------------------------

#### MandatoryExpenses

- user: Foreing Key to [Customuser](#customuser)
- amount: PositiveIntegerField

-------------------------------------------------------------------------

#### DeductionsFunds

- user: Foreing Key to [Customuser](#customuser)

-------------------------------------------------------------------------

## Cost app

Cost Tracing App

Allows you to add and track expenses, break them into categories and generate expense analytics.

### Basic entities:

#### Category

- name: Char
- limit: Decimal
- user_id: Foreing Key to [Customuser](#customuser)

-------------------------------------------------------------------------

#### Cost

- name: Char
- amount: Decimal
- created_at: DateTime
- category_id: Fofeing Key to [Category](#category)
- user_id: Foreing Key to [Customuser](#customuser)

-------------------------------------------------------------------------

## Cauth

Custom Authorization App

Implements user authorization by JWT, and represents the logic of interaction with the user profile.

### Basic entities:

#### CustomUser

- email: Email
- username: Char
- first_name: Char
- last_name: Char
- rate_plan: Choice
- is_active: Bool
- is_staff: Bool
- created_at: DateTime
- updated_at: DateTime