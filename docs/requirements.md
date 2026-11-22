# PayLink - Requirements Document

## 1. Problem Summary

PayLink is a digital wallet and bill-payment backend system designed to make bill payments easier, faster, and more reliable for customers in Egypt.

Currently, customers need a convenient way to pay their electricity, water, mobile, and internet bills without visiting the service providers' offices. PayLink aims to solve this problem by allowing customers to pay their bills using their digital wallet through a mobile application or authorized agents.

The system manages customer wallets, processes bill payments, communicates with biller companies, calculates service fees, and sends payment notifications.

PayLink must ensure that every transaction is handled correctly and securely. It must prevent duplicate payments, protect customers' money, and handle failed or delayed transactions by returning the appropriate amount to the customer's wallet when necessary.

The main goal is to build a reliable, secure, and extensible backend system that can support different biller companies and handle a large number of transactions.
## 2. Stakeholders

| Stakeholder | Role and Responsibility |
|---|---|
| Customers | Register, manage their wallets, view balances, inquire about bills, and make payments. |
| Agents | Help customers pay bills through PayLink terminals and receive commissions for successful payments. |
| Administrators | Manage billers, services, fees, payment limits, and system configurations. |
| Support Employees | Monitor transactions, investigate payment problems, search payment history, and manage account issues. |
| Biller Companies | Provide bill information and receive payments from PayLink, including electricity, water, mobile, and internet providers. |
| Management | Monitor business performance, transaction accuracy, revenue, and overall system reliability. |
| External Service Providers | Provide supporting services such as SMS, email, push notifications, and simulated payment processing. |
## 3. Functional Requirements

### FR-1: Customer Registration

**Priority:** Must

**User Story:**

As a customer, I want to create a PayLink account, so that I can use the digital wallet and bill-payment services.

**Acceptance Criteria:**

- **Scenario 1: Successful registration**
  - Given a customer who has not registered before
  - When the customer submits valid registration information
  - Then the system creates a new customer account
  - And assigns the Basic verification level to the account
  - And creates an empty wallet with available balance 0.00 EGP and held balance 0.00 EGP

- **Scenario 2: Duplicate registration**
  - Given a phone number that is already registered
  - When a customer tries to register with the same phone number
  - Then the system rejects the request with a clear error message
  - And no new account is created

### FR-2: View Wallet Balance and Transaction History

**Priority:** Must

**User Story:**

As a customer, I want to see my available balance, held balance and transaction history, so that I always know how much money I have and where it went.

**Acceptance Criteria:**

- **Scenario 1: View balances**
  - Given a customer with 400.00 EGP available and 352.50 EGP held
  - When the customer opens the wallet screen
  - Then the system shows the available balance and the held balance separately

- **Scenario 2: View transaction history**
  - Given a customer who has made top-ups and payments
  - When the customer requests the transaction history
  - Then the system lists the ledger entries from newest to oldest
  - And each entry shows type, amount, date and related payment reference

### FR-3: Top Up the Wallet

**Priority:** Must

**User Story:**

As a customer, I want to top up my wallet by simulated card or by agent cash, so that I have money to pay bills.

**Acceptance Criteria:**

- **Scenario 1: Top up by simulated card**
  - Given a customer with an active wallet
  - When the customer tops up 500.00 EGP using a simulated card
  - Then the system creates a TOPUP ledger entry of 500.00 EGP
  - And the available balance increases by 500.00 EGP

- **Scenario 2: Top up by agent cash**
  - Given a customer who gives 200.00 EGP cash to an agent
  - When the agent submits the top-up for the customer
  - Then the customer's available balance increases by 200.00 EGP
  - And the operation is recorded in the audit log with the agent identity

- **Scenario 3: Invalid amount**
  - Given a customer with an active wallet
  - When the customer tries to top up zero or a negative amount
  - Then the system rejects the request
  - And the balance does not change

 ### FR-4: Ledger-Based Balances

**Priority:** Must

**User Story:**

As the company, I want every balance change recorded as a ledger entry and balances computed from the ledger, so that money is always traceable and never overwritten.

**Acceptance Criteria:**

- **Scenario 1: Every change creates an entry**
  - Given any operation that changes money (top-up, hold, hold release, charge, fee income, commission, refund)
  - When the operation is executed
  - Then the system creates a LedgerEntry with type, amount, wallet and timestamp

- **Scenario 2: Balance equals sum of entries**
  - Given a wallet with several ledger entries
  - When the balance is calculated
  - Then the available balance and the held balance equal the sums of the related entries

- **Scenario 3: No direct overwrite**
  - Given an existing wallet
  - When any module needs to change a balance
  - Then it can only do so by adding a new ledger entry
  - And existing ledger entries are never edited or deleted

 ### FR-5: Manage Billers and Services

**Priority:** Must

**User Story:**

As an admin, I want to add, edit and disable billers and services, so that I can control what customers are able to pay.

**Acceptance Criteria:**

- **Scenario 1: Add a biller or service**
  - Given a logged-in admin
  - When the admin submits a new biller or service with valid data (name, required fields, min and max amounts)
  - Then the system saves it and shows it in the catalog

- **Scenario 2: Edit a biller or service**
  - Given an existing service
  - When the admin changes its minimum or maximum amount
  - Then the new values are used for the next payments

- **Scenario 3: Disable a biller**
  - Given an active biller
  - When the admin disables it
  - Then customers can no longer start payments to it
  - And payments already in progress are not affected

- **Scenario 4: Non-admin access**
  - Given a user who is not an admin
  - When the user tries to add, edit or disable a biller
  - Then the system rejects the request with an authorization error

### FR-6: View Billers and Required Fields

**Priority:** Must

**User Story:**

As a customer, I want to see the list of billers and the input fields each one requires, so that I know what information to enter before paying.

**Acceptance Criteria:**

- **Scenario 1: List active billers**
  - Given billers ElectroCo, AquaCo and TopUpNet are active
  - When the customer opens the biller list
  - Then the system shows each biller with its services

- **Scenario 2: Show required fields**
  - Given the customer selects the ElectroCo electricity service
  - When the service details are displayed
  - Then the system shows the required input field "meter number"
  - And for TopUpNet it shows "phone number"

- **Scenario 3: Hide disabled billers**
  - Given a disabled biller
  - When the customer opens the biller list
  - Then the disabled biller is not shown

### FR-7: Bill Inquiry

**Priority:** Must

**User Story:**

As a customer, I want to run a bill inquiry and see the amount, fee and total before paying, so that I know exactly what I will be charged.

**Acceptance Criteria:**

- **Scenario 1: Successful inquiry**
  - Given a customer enters a valid meter number for ElectroCo
  - When the customer requests a bill inquiry
  - Then the system gets the bill from ElectroCo and shows amount 350.00 EGP
  - And shows the service fee 2.50 EGP
  - And shows the total 352.50 EGP

- **Scenario 2: Invalid account number**
  - Given a meter number that the biller does not know
  - When the customer requests a bill inquiry
  - Then the system shows a clear "bill not found" message
  - And no payment is created

- **Scenario 3: Biller unavailable**
  - Given the biller does not answer
  - When the customer requests a bill inquiry
  - Then the system shows a clear "service temporarily unavailable" message
  - And other billers keep working normally

### FR-8: Pay a Bill from the Wallet

**Priority:** Must

**User Story:**

As a customer, I want to pay a bill from my wallet, so that I do not have to queue at the biller's office.

**Acceptance Criteria:**

- **Scenario 1: Successful payment**
  - Given Sara has 400.00 EGP available and a bill of 350.00 EGP with a 2.50 EGP fee
  - When Sara confirms the payment
  - Then the system holds 352.50 EGP from her available balance
  - And sends the payment to the biller
  - And when the biller confirms, the payment becomes Completed

- **Scenario 2: Insufficient funds**
  - Given a customer with 100.00 EGP available and a total of 352.50 EGP
  - When the customer confirms the payment
  - Then the payment becomes Rejected with the reason "insufficient funds"
  - And the biller is not called

- **Scenario 3: Failed payment**
  - Given a payment in SentToBiller state
  - When the biller refuses the payment
  - Then the payment becomes Failed
  - And the held money is released back to the wallet

### FR-9: Idempotent Payment Requests

**Priority:** Must

**User Story:**

As a customer, I want a repeated request to be treated as the same payment, so that I am never charged twice when my network is slow.

**Acceptance Criteria:**

- **Scenario 1: Same key sent twice**
  - Given a payment request with idempotency key K that was already processed
  - When the mobile app sends the same request with key K again
  - Then the system returns the original result
  - And no second payment or second charge is created

- **Scenario 2: Same key sent at the same moment**
  - Given two identical requests with key K arrive at the same time
  - When both are processed
  - Then only one payment is created
  - And both requests receive the same result

- **Scenario 3: New key**
  - Given a request with a key that was never used
  - When the request is processed
  - Then the system creates a new payment and stores the key with its result

### FR-10: Payment Life Cycle

**Priority:** Must

**User Story:**

As the company, I want every payment to follow the allowed life cycle and no other transitions, so that payment states are always correct and predictable.

**Acceptance Criteria:**

- **Scenario 1: Allowed transition**
  - Given a payment in state FundsHeld
  - When the request is sent to the biller
  - Then the payment becomes SentToBiller

- **Scenario 2: Forbidden transition**
  - Given a payment in state Completed
  - When any event tries to change it to Failed
  - Then the system refuses the transition
  - And the payment stays Completed

- **Scenario 3: Final states**
  - Given a payment in Completed, Rejected or Refunded
  - When any event arrives for it
  - Then the state does not change

- **Scenario 4: State history**
  - Given any state change
  - When the change happens
  - Then the system records a PaymentEvent with the old state, the new state and the time

### FR-11: Hold Funds Before Calling the Biller

**Priority:** Must

**User Story:**

As the company, I want funds held before the biller is called and released if the payment fails, so that customers cannot spend the same money twice and are not charged for failed payments.

**Acceptance Criteria:**

- **Scenario 1: Hold first**
  - Given a payment in state Initiated that passed the checks
  - When the system prepares to call the biller
  - Then 352.50 EGP is moved from available balance to held balance first
  - And only then the payment is sent to the biller

- **Scenario 2: Release on failure**
  - Given a payment that became Failed
  - When the system processes the failure
  - Then the hold is released to the available balance
  - And the payment becomes Refunded

- **Scenario 3: Convert on success**
  - Given a payment that became Completed
  - When the system processes the confirmation
  - Then the hold becomes a final CHARGE
  - And the service fee is credited as FEE_INCOME

### FR-12: Timeout Handling and Retries

**Priority:** Must

**User Story:**

As a customer, I want a payment that gets no answer to stay safe and be checked again, so that I am neither charged twice nor refunded by mistake.

**Acceptance Criteria:**

- **Scenario 1: Timeout**
  - Given a payment in SentToBiller and a live biller that takes 12 seconds to answer
  - When the 10-second timeout passes
  - Then the payment becomes Unknown
  - And the customer is told the payment is being processed
  - And the money stays held

- **Scenario 2: Re-query**
  - Given a payment in Unknown state
  - When 1, 5 and 15 minutes have passed
  - Then the system re-queries the biller at each time (3 times in total)

- **Scenario 3: Later confirmation or refusal**
  - Given a payment in Unknown state
  - When a re-query returns "paid"
  - Then the payment becomes Completed
  - And when a re-query returns "refused" the payment becomes Failed

- **Scenario 4: No automatic refund**
  - Given a payment still in Unknown after 3 re-queries
  - When no answer was received
  - Then the system keeps the money held and waits for reconciliation
  - And does not refund automatically

### FR-13: Asynchronous Callbacks from TopUpNet

**Priority:** Must

**User Story:**

As the company, I want to accept TopUpNet callbacks and ignore duplicates, so that a mobile top-up is completed exactly once.

**Acceptance Criteria:**

- **Scenario 1: Callback "success"**
  - Given a TopUpNet payment that was "accepted" and is waiting
  - When TopUpNet calls the callback URL with "success"
  - Then the payment becomes Completed

- **Scenario 2: Callback "failed"**
  - Given a TopUpNet payment that is waiting
  - When TopUpNet calls the callback URL with "failed"
  - Then the payment becomes Failed and the hold is released

- **Scenario 3: Duplicate callback**
  - Given a payment that is already Completed
  - When TopUpNet sends "success" a second time
  - Then the payment is not completed again
  - And the duplicate is ignored and written to the log

### FR-14: Support Billers with Different Formats

**Priority:** Must

**User Story:**

As the company, I want to support billers with different protocols, so that customers can pay electricity, water and mobile top-up bills.

**Acceptance Criteria:**

- **Scenario 1: ElectroCo**
  - Given an ElectroCo payment
  - When the system calls the biller
  - Then it uses REST with JSON and gets an immediate answer

- **Scenario 2: AquaCo**
  - Given an AquaCo payment
  - When the system calls the biller
  - Then it uses SOAP-style XML over HTTP
  - And maps AquaCo's error codes to PayLink's own reasons

- **Scenario 3: TopUpNet**
  - Given a TopUpNet payment
  - When the system calls the biller
  - Then it uses REST with JSON and waits for the asynchronous callback

- **Scenario 4: Biller isolation**
  - Given one biller is down
  - When customers pay other billers
  - Then those payments work normally

### FR-15: Fee Calculation

**Priority:** Must

**User Story:**

As the company, I want fees calculated by the configured rules including promotions, so that every payment is charged the correct fee.

**Acceptance Criteria:**

- **Scenario 1: Fixed fee**
  - Given an electricity or water payment
  - When the fee is calculated
  - Then the fee is 2.50 EGP

- **Scenario 2: Percentage fee**
  - Given a mobile top-up of 50.00 EGP
  - When the fee is calculated
  - Then the fee is 1.5% of the amount with a minimum of 1 EGP, which is 1.00 EGP

- **Scenario 3: Tiered fee**
  - Given an internet payment of 150.00 EGP and another of 300.00 EGP
  - When the fee is calculated
  - Then the first fee is 2.00 EGP and the second is 4.00 EGP

- **Scenario 4: Promotion**
  - Given a promotion for one chosen biller between a start date and an end date
  - When a payment to that biller is made inside the period
  - Then the fee is 0.00 EGP
  - And outside the period the normal fee applies

### FR-16: Agent Pays on Behalf of a Customer

**Priority:** Should

**User Story:**

As an agent, I want to pay a bill on behalf of a customer and earn a commission, so that I am rewarded for serving customers at my shop.

**Acceptance Criteria:**

- **Scenario 1: Agent payment**
  - Given a registered agent and a customer with enough balance
  - When the agent submits a payment for the customer
  - Then the payment is created with the agent recorded as the source
  - And it follows the same life cycle and checks as a normal payment

- **Scenario 2: Commission on completion**
  - Given an agent payment with a service fee of 2.50 EGP
  - When the payment becomes Completed
  - Then 1.00 EGP (40% of the fee) is credited to the agent's wallet as a COMMISSION ledger entry
  - And a Commission record is created

- **Scenario 3: No commission on failure**
  - Given an agent payment that became Failed
  - When the hold is released
  - Then no commission is paid

### FR-17: Velocity Rule

**Priority:** Should

**User Story:**

As the company, I want an account that makes too many payments too fast to be blocked temporarily, so that stolen accounts and bots cannot drain wallets.

**Acceptance Criteria:**

- **Scenario 1: Block after too many payments**
  - Given an account that made 5 payments in the last 60 seconds
  - When the account tries a 6th payment
  - Then the payment becomes Rejected with the reason "too many payments"
  - And the account is blocked for 10 minutes

- **Scenario 2: Payments during the block**
  - Given a temporarily blocked account
  - When the customer tries to pay
  - Then the payment becomes Rejected with the reason "account blocked"

- **Scenario 3: Block expires**
  - Given an account blocked for 10 minutes
  - When 10 minutes have passed
  - Then the account can pay again

### FR-18: Block and Unblock an Account

**Priority:** Should

**User Story:**

As a support employee, I want to block and unblock an account, so that I can stop suspicious activity quickly.

**Acceptance Criteria:**

- **Scenario 1: Block**
  - Given an active account
  - When a support employee blocks it with a reason
  - Then every new payment from the account is Rejected
  - And the action is written to the audit log

- **Scenario 2: Unblock**
  - Given a blocked account
  - When a support employee unblocks it
  - Then the account can pay again

- **Scenario 3: Unauthorized user**
  - Given a user who is not a support employee or admin
  - When the user tries to block an account
  - Then the system rejects the request with an authorization error

### FR-19: Notification Retry

**Priority:** Should

**User Story:**

As the company, I want failed notifications retried and finally marked undelivered, so that temporary provider problems do not lose messages.

**Acceptance Criteria:**

- **Scenario 1: Retry**
  - Given an SMS that failed to send
  - When the retry runs
  - Then the system tries again up to 3 times
  - And the NotificationLog shows the number of attempts

- **Scenario 2: Success on retry**
  - Given an SMS that failed once
  - When the second attempt succeeds
  - Then the status becomes SENT and no more retries run

- **Scenario 3: Undelivered**
  - Given an SMS that failed all 3 retries
  - When the last retry fails
  - Then the status becomes UNDELIVERED
  - And the payment state is not affected

### FR-20: Edit Fees and Limits Without Redeploying

**Priority:** Should

**User Story:**

As an admin, I want to edit fee and limit values without redeploying, so that business changes do not need a new release.

**Acceptance Criteria:**

- **Scenario 1: Change a value**
  - Given a logged-in admin
  - When the admin changes the daily limit of Basic accounts to 6,000 EGP
  - Then the new value is used for payments after the change
  - And the system is not restarted

- **Scenario 2: Audit**
  - Given a configuration change
  - When it is saved
  - Then an AuditLog record shows who changed it, the old value and the new value

- **Scenario 3: Invalid value**
  - Given an admin enters a negative limit or fee
  - When the admin saves
  - Then the system rejects the change and keeps the old value

- **Scenario 4: Promotion dates**
  - Given an admin sets a promotion for one biller with start and end dates
  - When the dates are saved
  - Then the fee is 0.00 EGP for that biller only inside the period

### FR-21: Audit Log

**Priority:** Must

**User Story:**

As the company, I want every money movement and admin action written to an audit log, so that we can show who did what, when and why to auditors and regulators.

**Acceptance Criteria:**

- **Scenario 1: Money movement**
  - Given any ledger entry is created
  - When the operation is saved
  - Then an AuditLog record is created with who, when, why and the amount

- **Scenario 2: Admin action**
  - Given an admin disables a biller or changes a fee
  - When the action is saved
  - Then an AuditLog record shows the admin identity, the old value and the new value

- **Scenario 3: Immutable log**
  - Given existing audit records
  - When anyone tries to edit or delete one
  - Then the system refuses

### FR-22: Notifications on Completion and Failure

**Priority:** Must

**User Story:**

As a customer, I want an SMS and a push notification when my payment completes or fails, so that I know the result immediately.

**Acceptance Criteria:**

- **Scenario 1: Completion**
  - Given a payment that became Completed
  - When the system processes the confirmation
  - Then the customer receives an SMS and a push message with the receipt

- **Scenario 2: Failure**
  - Given a payment that became Failed
  - When the system processes the failure
  - Then the customer receives an SMS with a clear reason

- **Scenario 3: SMS provider down**
  - Given the SMS provider is down when a payment completes
  - When the system tries to send the SMS
  - Then the payment still stays Completed
  - And the SMS is retried and finally marked undelivered if it keeps failing

### FR-23: Support Search of Payments

**Priority:** Must

**User Story:**

As a support employee, I want to search a payment by its reference and see its full history, so that I can answer customer complaints.

**Acceptance Criteria:**

- **Scenario 1: Search by reference**
  - Given a payment with reference P-1001
  - When a support employee searches for P-1001
  - Then the system shows the payment details (amount, fee, biller, customer, current state)

- **Scenario 2: Full history**
  - Given the same payment
  - When the support employee opens it
  - Then the system shows all PaymentEvents, ledger entries and notifications related to it

- **Scenario 3: Not found**
  - Given a reference that does not exist
  - When the support employee searches
  - Then the system shows "payment not found"

### FR-24: Customer Refund Request

**Priority:** Could

**User Story:**

As a customer, I want to request a refund of a completed payment and have support approve it, so that I can recover money from payments made by mistake.

**Acceptance Criteria:**

- **Scenario 1: Request**
  - Given a customer with a Completed payment
  - When the customer submits a refund request with a reason
  - Then a Refund record is created with status Pending
  - And support is notified

- **Scenario 2: Approval**
  - Given a pending refund request
  - When a support employee approves it
  - Then a REFUND ledger entry returns the money to the wallet
  - And the action is written to the audit log

- **Scenario 3: Rejection**
  - Given a pending refund request
  - When a support employee rejects it with a reason
  - Then no money moves and the customer is notified

### FR-25: Admin Daily Totals

**Priority:** Could

**User Story:**

As an admin, I want to see daily totals of payments, fees earned, commissions paid and failures per biller, so that I can monitor the business.

**Acceptance Criteria:**

- **Scenario 1: Daily totals**
  - Given a day with completed payments
  - When the admin opens the daily totals
  - Then the system shows the number and sum of payments, the fees earned and the commissions paid

- **Scenario 2: Failures per biller**
  - Given failed payments for several billers
  - When the admin opens the totals
  - Then the failures are shown grouped by biller

- **Scenario 3: Non-admin access**
  - Given a user who is not an admin
  - When the user tries to open the totals
  - Then the system rejects the request

## 4. Non-Functional Requirements

| ID | Quality | Requirement | How we measure it | Target | Priority |
|---|---|---|---|---|---|
| NFR-1 | Correctness | No customer is ever charged twice for the same payment | Automated tests: duplicate requests (same idempotency key) and 50 concurrent identical requests | 0 double charges | Must |
| NFR-2 | Correctness | A wallet balance never becomes negative | Concurrency test: 2 payments at the same moment, balance covers only one | 0 negative balances; 1 payment succeeds, 1 Rejected | Must |
| NFR-3 | Performance | The system handles a high load of payments against the mock billers | Load test (k6 or Locust), 100 payments/second for 1 minute | At least 100 payments/s sustained; error rate below 1% | Should |
| NFR-4 | Resilience | An outage of one biller does not stop payments to other billers | Test: stop AquaCo mock, pay ElectroCo and TopUpNet | 100% of payments to healthy billers succeed | Must |
| NFR-5 | Modifiability | Adding a new biller touches only the Biller Integration module and configuration | Count of changed files outside biller_integration and config when adding a biller (git diff) | 0 files changed in other modules | Must |
| NFR-6 | Auditability | Every money movement has an audit record with who, when and why | Test comparing the number of LedgerEntry rows with AuditLog rows | 100% coverage (1 audit record per ledger entry) | Must |
| NFR-7 | Testability | Domain logic is covered by automated tests | Coverage report in the CI pipeline | At least 70% line coverage on domain logic | Must |

## 5. Questions, Ambiguities and Decisions

| # | Question / ambiguity | Where found | Decision | Reason |
|---|---|---|---|---|
| Q1 | Does the daily limit count the service fee or only the bill amount? | Brief 2.6 | Only the bill amount | The limit is described as a "payment" limit; simpler to explain to customers |
| Q2 | Is a payment of exactly 5,000 EGP accepted for a Basic account on a fresh day? | Brief 2.6 | Yes. A payment is rejected only when the daily total would be MORE than the limit | "Limit" means the maximum allowed value |
| Q3 | Does the single-payment limit (10,000 EGP) apply to the bill amount or to the total with fee? | Brief 2.6 | Bill amount | Same reason as Q1 |
| Q4 | Which "day" is used for the daily limit (calendar day or last 24 hours)? | Brief 2.6 | Calendar day in Africa/Cairo time, starting at 00:00 | Easy to explain and to test |
| Q5 | Does the daily limit count Rejected and Failed payments? | Brief 2.6 | No. Only Completed payments and payments still in progress (FundsHeld, SentToBiller, Unknown) | Money that returned to the wallet should not use the limit |
| Q6 | Is the commission returned if an agent payment later fails? | Brief 2.6, FR-16 | Commission is paid only when the payment is Completed, so a Failed payment has no commission | Matches "credited when the payment completes" |
| Q7 | Does the velocity rule (more than 5 payments in 60 s) apply to agents too? | Brief 2.6, FR-17 | Yes, it applies to the account that sends the payment | Agent accounts can also be abused |
| Q8 | Can a customer get a refund for a Completed payment, since Completed is a final state? | Brief 2.5, FR-24 | Yes, but as a separate Refund record with a REFUND ledger entry. The Payment state stays Completed | Section 2.5 forbids changing a Completed payment |
| Q9 | What happens if a promotion ends while a payment is in progress? | Brief 2.6, FR-15 | The fee is calculated once, when the payment is created, and never changes afterwards | Avoids changing the amount after money is held |
| Q10 | After 3 re-queries a payment is still Unknown. Who resolves it? | Brief 2.5, FR-12 | It stays Unknown with the money held until a later callback or reconciliation. It is never refunded automatically | The brief says Unknown is never refunded automatically |
