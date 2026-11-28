"""PayPilot money guides, part C: cash flow, freelancers, credit cards, alternatives."""

GUIDES_C = [
{
"slug": "safe-to-spend-calculator",
"title": "Safe to Spend: Income, Cash Flow and the Number Worth Checking",
"desc": "Why your bank balance misleads you, how to work out safe to spend from income, bills and spending, and why transfers and refunds are not income.",
"category": "Cash flow",
"tags": "Tracking",
"lede": "Your bank balance answers \"how much money is in the account right now?\" It does not answer the question you actually have, which is \"how much can I spend without trouble before next payday?\" Safe to spend is the answer to that one.",
"sections": [
("quick-answer", "Quick answer", """
<p>Safe to spend = money received this period − money already spent − bills still due before the next income − what you have decided to save. Divide the result by the days left to get a daily figure. Check it before a big purchase, not after.</p>
"""),
("balance", "Why the balance misleads", """
<p>Payday is the moment your balance is highest and least honest. Rent, the card bill, school fees and subscriptions have not left yet, but they are already spoken for. People overspend in the first week after payday for exactly this reason, then feel squeezed in the last.</p>
"""),
("example", "A worked example", """
<p>It is the 10th. You were paid ₹85,000 on the 1st.</p>
<table><thead><tr><th></th><th>Amount</th></tr></thead><tbody>
<tr><td>Income this month</td><td>₹85,000</td></tr>
<tr><td>Spent so far</td><td>− ₹24,000</td></tr>
<tr><td>Bills still due (rent ₹22,000, EMI ₹9,500, broadband ₹800, insurance ₹2,700)</td><td>− ₹35,000</td></tr>
<tr><td>Planned savings (SIP)</td><td>− ₹10,000</td></tr>
<tr><td><strong>Safe to spend for the rest of the month</strong></td><td><strong>₹16,000</strong></td></tr>
<tr><td>Days left (to the 31st)</td><td>21</td></tr>
<tr><td><strong>Per day</strong></td><td><strong>about ₹760</strong></td></tr>
</tbody></table>
<p>Your bank app would show ₹61,000 on the 10th. The honest number is ₹16,000. Both are correct; only one helps you decide whether to buy the new headphones.</p>
"""),
("income", "Income: what counts and what does not", """
<p>A safe-to-spend figure is only as good as the income line, and that line is easy to inflate by accident.</p>
<ul>
<li><strong>Income:</strong> salary, freelance payments, rent you receive, interest, a bonus.</li>
<li><strong>Not income:</strong> transfers from your own savings account, a refund (it reduces the original expense), a friend repaying a loan (it reduces what they owe you), or money moved from a card or wallet.</li>
</ul>
<p>Counting a refund or a loan repayment as income makes you look richer than you are, which is the opposite of what this number is for.</p>
"""),
("cashflow", "Cash flow: money in versus money out", """
<p>Once income and spending are both recorded, a monthly cash-flow view answers three questions an expense list cannot:</p>
<ol class="steps">
<li><strong>Net:</strong> did more come in than went out this month?</li>
<li><strong>Committed:</strong> how much of next month is already promised to rent, EMIs and subscriptions?</li>
<li><strong>Trend:</strong> is the gap between in and out growing or shrinking over several months?</li>
</ol>
<p>Timing matters too. If your salary lands on the 28th and rent goes on the 1st, the month boundary makes both months look wrong. Look at the period from one payday to the next, not the calendar month.</p>
"""),
("try", "Try the numbers", """
<p>The free <a href="../budget-calculator">salary budget and safe-to-spend calculator</a> works this out in AED or INR from your salary, bills and savings goal, with no sign-up.</p>
"""),
("paypilot", "Safe to spend in PayPilot", """
<p>Spending and recurring bills are tracked in the free app. PayPilot Credit, an optional one-time purchase with no subscription, adds income tracking, your net each month, a safe-to-spend figure that subtracts upcoming bills automatically, and cash-flow reports and statements. Income from bank SMS such as salary credits is logged automatically once Credit is unlocked.</p>
"""),
],
"faq": [
("What is a good safe-to-spend amount?", "There is no universal number. What matters is that it stays positive until your next income. If it goes negative mid-month, something in the plan needs to change."),
("Should savings be subtracted before safe to spend?", "Yes. Treat savings like a bill that is due on payday. Otherwise it becomes whatever is left over, which is usually nothing."),
("Is a refund income?", "No. A refund reverses part of an earlier expense. Record it against that expense rather than as income."),
],
"related": ["dubai-salary-budget", "freelancer-variable-income-tracker", "subscription-tracker-monthly-bills"],
},
{
"slug": "freelancer-variable-income-tracker",
"title": "Budgeting on Variable Income: A System for Freelancers",
"desc": "A budget that survives quiet months: baseline income, paying yourself from a buffer, setting tax aside, and separating business and personal spending.",
"category": "Freelancers",
"tags": "Tracking",
"lede": "A salary budget assumes the same amount arrives on the same day every month. Freelance income does neither. The answer is not a more detailed budget. It is a buffer between the money that comes in and the money you live on.",
"sections": [
("quick-answer", "Quick answer", """
<p>Budget your personal life on your lowest normal month, not your average. Send every client payment into a holding account, set a share aside for tax, and pay yourself a fixed monthly amount from what remains. Good months fill the buffer; quiet months draw on it.</p>
"""),
("baseline", "Step 1: find your baseline", """
<p>List what you earned in each of the last 12 months, after business costs. Ignore the single worst month if it was a genuine one-off, such as illness or a move. The lowest remaining month is your baseline. Your fixed personal costs (rent, EMIs, insurance, groceries) need to fit inside it.</p>
<table><thead><tr><th>Month</th><th>Earned</th></tr></thead><tbody>
<tr><td>Best month</td><td>AED 24,000</td></tr>
<tr><td>Average</td><td>AED 14,500</td></tr>
<tr><td>Lowest normal month</td><td>AED 9,000</td></tr>
</tbody></table>
<p>Planning on the AED 14,500 average means four or five months a year where the money runs out. Planning on AED 9,000 means good months build a cushion instead of a lifestyle.</p>
"""),
("buffer", "Step 2: pay yourself from a buffer", """
<ol class="steps">
<li>Every client payment goes into one account that you do not spend from directly.</li>
<li>Set the tax share aside first (see below).</li>
<li>On the same day each month, move your fixed "salary" (your baseline) to your everyday account.</li>
<li>When the buffer holds three months of salary, start moving the surplus to savings or investments.</li>
</ol>
<p>The first few months are the hardest, because the buffer starts empty. A month or two of living below your baseline to build it is worth it.</p>
"""),
("tax", "Step 3: set tax aside as money arrives", """
<p>Tax rules for freelancers differ by country and by your situation, so get advice for the details. The habit that works everywhere is to move a fixed percentage of every payment into a separate tax pot the day it arrives, so the money is there when the bill comes.</p>
<ul>
<li><strong>India:</strong> freelancers whose tax for the year exceeds the threshold usually pay advance tax in instalments during the year, due in June, September, December and March.</li>
<li><strong>UAE:</strong> there is no personal income tax, but a freelancer operating under a business licence may fall under corporate tax and VAT registration rules depending on income. Check with an adviser.</li>
</ul>
"""),
("separate", "Step 4: separate business and personal spending", """
<p>Software, equipment, co-working, travel to clients and professional fees are business costs. Groceries are not, even if you eat them at your desk. Keeping them apart (a separate card helps) makes tax time easier and shows whether the business itself is profitable, which is a different question from whether you are saving money.</p>
"""),
("quiet", "When a quiet month comes", """
<p>If you have a buffer, a quiet month is a non-event: you pay yourself as usual. Without one, cut in this order: occasional spending first, then subscriptions, then everyday spending. Do not stop the tax pot, and avoid covering the gap with a credit card you cannot clear next month.</p>
"""),
("paypilot", "Doing this in PayPilot", """
<p>Log client payments as income (with PayPilot Credit) and business costs under their own categories, so the monthly net shows what you really earned. Recurring costs such as software subscriptions sit in the Payments tab with reminders. The <a href="../budget-calculator">budget calculator</a> helps you test whether your fixed costs fit inside your baseline.</p>
"""),
],
"faq": [
("How big should a freelancer's buffer be?", "Three months of your personal salary is a common target. If your income is very seasonal, aim higher."),
("What percentage should I set aside for tax?", "It depends on your income, country and deductions. Ask an adviser for a figure, then set that percentage aside from every payment."),
("Should I use a separate account for business?", "It helps a lot. Even a second card used only for business costs makes tracking and tax much simpler."),
],
"related": ["safe-to-spend-calculator", "subscription-tracker-monthly-bills", "dubai-salary-budget"],
},
{
"slug": "credit-card-spending-tracker",
"title": "Credit Card Spending Tracker: Stay Ahead of the Statement",
"desc": "Track card spending before the bill arrives: statement cycles, interest-free periods, the minimum payment trap, instalment plans and foreign fees.",
"category": "Credit cards",
"tags": "Tracking",
"lede": "A credit card separates the moment you buy from the moment you pay, sometimes by seven weeks. That gap is useful, but it is also why card spending feels unreal until the statement lands. Tracking purchases as they happen closes the gap.",
"sections": [
("quick-answer", "Quick answer", """
<p>Record each card purchase as an expense on the day you make it, and treat paying the card bill as a transfer, not a second expense. Keep a running total for the current statement cycle, and pay the full statement balance by the due date whenever you can.</p>
"""),
("cycle", "Statement date versus due date", """
<p>Every card has two dates. The <strong>statement date</strong> closes the cycle: everything bought before it appears on this bill. The <strong>due date</strong>, usually a few weeks later, is when payment is due. A purchase made just after the statement date might not need paying for well over a month; one made just before it is due in a few weeks.</p>
<p>That is the interest-free period, and it only works if you pay the full statement balance. Pay less, and most cards charge interest, often from the purchase date, at rates far higher than a personal loan. Check your card's terms for the exact rules.</p>
"""),
("minimum", "The minimum payment trap", """
<p>Paying only the minimum due keeps your account in good standing, but the rest of the balance keeps collecting interest. On a large balance, minimum payments can take years to clear it and cost more in interest than the original purchases. If you cannot pay in full, pay as much as you can, and stop adding new spending to that card until it is clear.</p>
"""),
("track", "How to track a card properly", """
<ol class="steps">
<li>Log every purchase as an expense on the day, with the card it was on.</li>
<li>Keep a running total for the current cycle, and compare it with what you can pay in full on the due date.</li>
<li>When you pay the bill, record it as a transfer from your bank account to the card. It is not new spending.</li>
<li>Check refunds land: a returned item should reduce the card balance, not disappear.</li>
</ol>
<p>The most common mistake is counting both the purchase and the bill payment as spending, which doubles your card spending in the budget.</p>
"""),
("instalments", "Instalment plans and foreign charges", """
<p>Converting a purchase into instalments (EMIs) spreads the cost, but check the processing fee and any interest. Record the purchase once, then the monthly instalment as a recurring commitment. The <a href="../emi-calculator">EMI calculator</a> shows the real cost.</p>
<p>Paying in a foreign currency usually adds a foreign transaction fee, often a few percent of the amount. If a foreign shop or website offers to charge you in your home currency, compare the rate first; that conversion is often worse than letting your card convert it.</p>
"""),
("several", "Juggling two or three cards", """
<p>Many people carry one card for rewards, one for a specific shop or airline, and one backup. Note each card's statement and due dates in one place. When purchases are tagged with the card's last four digits, you can see each card's running total at a glance, and choose which card to use for a big purchase based on where each one is in its cycle.</p>
"""),
("paypilot", "Credit card tracking in PayPilot", """
<p>Card purchases are captured from your bank's SMS, app notifications or Apple Pay, and each record keeps the card's last four digits. Card bills and instalments can be added as recurring payments with reminders before the due date. This is all part of the free app.</p>
"""),
],
"faq": [
("Is paying my credit card bill an expense?", "No. The purchases were the expenses. Paying the bill moves money from your bank account to the card, so record it as a transfer."),
("How do I avoid credit card interest?", "Pay the full statement balance by the due date every month. Check your card's terms, as rules for cash withdrawals and instalment plans differ."),
("Should I convert big purchases to instalments?", "Only if you need to spread the cost and you have checked the total fees and interest. A 0% plan with a processing fee still costs something."),
],
"related": ["dubai-salary-budget", "subscription-tracker-monthly-bills", "loan-tracker-money-lent"],
},
{
"slug": "money-manager-alternative-automatic",
"title": "Money Manager, Wallet or a Spreadsheet? Choosing How to Track Expenses",
"desc": "An honest comparison of spreadsheets, manual apps like Money Manager, bank-sync apps like Wallet, and alert-based trackers, plus how to switch cleanly.",
"category": "Comparisons",
"tags": "Comparisons Tracking",
"lede": "There are four broad ways to track spending, and each one fails in a different way. The best one for you is the one you will still be using in six months, so it helps to know which failure you are most likely to hit.",
"sections": [
("quick-answer", "Quick answer", """
<p>If you enjoy building your own system, a spreadsheet gives the most control. If you are happy typing every expense, a manual ledger app like Money Manager is fast and simple. If you want automation and do not mind connecting your bank, a bank-sync app like Wallet covers more accounts. If you want automation without a bank connection, an alert-based tracker reads the payment alerts already on your phone.</p>
"""),
("compare", "The four approaches side by side", """
<table><thead><tr><th></th><th>Spreadsheet</th><th>Manual ledger app</th><th>Bank-sync app</th><th>Alert-based app</th></tr></thead><tbody>
<tr><td>Example</td><td>Excel, Google Sheets</td><td>Money Manager</td><td>Wallet by BudgetBakers</td><td>PayPilot</td></tr>
<tr><td>How spending gets in</td><td>You type it</td><td>You type it, quickly</td><td>Imported from connected accounts</td><td>Read from SMS, notifications, Apple Pay</td></tr>
<tr><td>Bank connection</td><td>No</td><td>No</td><td>Yes, where supported</td><td>No</td></tr>
<tr><td>Flexibility</td><td>Total</td><td>Good</td><td>Good</td><td>Good</td></tr>
<tr><td>Where it usually fails</td><td>You stop updating it</td><td>You stop typing</td><td>Connections expire or your bank is not supported</td><td>A bank changes its alert wording</td></tr>
</tbody></table>
<p>Features and coverage of other apps change, so check their current versions. The point here is the approach, not a feature-by-feature scorecard.</p>
"""),
("spreadsheet", "When a spreadsheet is still the right answer", """
<p>A spreadsheet is unbeatable if you want custom categories and formulas, if you are tracking something unusual (a shared house fund, a renovation, a wedding), or if you like the act of reviewing every line. Its weakness is capture: typing transactions in at the end of the week is the step people abandon. Some people keep both: an app for capture, and a monthly export into a spreadsheet for analysis.</p>
"""),
("manual", "If you like Money Manager but are tired of typing", """
<p>Manual ledger apps are fast for each entry, but you still make every entry, and the ones you forget are usually small card and UPI payments. If that is your problem, the switch that helps is not more categories. It is capture: letting payment alerts create the records, and spending your attention on correcting a category now and then.</p>
"""),
("banksync", "If you are weighing Wallet or another bank-sync app", """
<p>Bank sync gives the widest coverage when your banks are supported, including accounts that do not send alerts. The trade-off is access: the app, or a provider it uses, holds a live connection to your accounts and full transaction history. If your banks are not supported, or you would rather not connect them, alert-based tracking gets most of the benefit with less access. Our <a href="is-sms-expense-tracker-safe">privacy comparison</a> goes into the differences.</p>
"""),
("switch", "How to switch without losing history", """
<ol class="steps">
<li>Export your old data to CSV, if the app allows it, and keep the file.</li>
<li>Start the new app on the first day of a month, or your next payday, rather than mid-cycle.</li>
<li>Set up recurring payments first, then automatic capture.</li>
<li>Run both side by side for one month if you want reassurance, then stop the old one.</li>
<li>Do not try to re-enter years of history. A clean start with good records beats a perfect archive you never look at.</li>
</ol>
"""),
("paypilot", "Where PayPilot fits", """
<p>PayPilot is an alert-based tracker for iPhone and Android. It reads payment SMS and app notifications on the phone, captures Apple Pay taps on iPhone, never connects to your bank, and keeps records on your device with encrypted sync if you sign in. Recurring payments, subscriptions, loans, budgets and automatic capture are free; income and cash-flow reports are a one-time purchase.</p>
"""),
],
"faq": [
("Is PayPilot a good Money Manager alternative?", "If your main frustration with Money Manager is typing every expense, yes: PayPilot creates records from payment alerts. If you prefer full manual control, a ledger app may still suit you better."),
("Can I move my data from another app?", "Keep an export of your old data for reference. Starting fresh from a clear date is usually easier than re-entering history."),
("Is a spreadsheet better than an app?", "It is more flexible, but harder to keep up to date. Many people use an app to capture spending and a spreadsheet for occasional analysis."),
],
"related": ["is-sms-expense-tracker-safe", "automatic-expense-tracker-bank-sms", "best-expense-tracker-app-uae"],
},
]

REDIRECTS = {
    "free-budget-app-uae": "best-expense-tracker-app-uae",
    "track-expenses-in-aed": "best-expense-tracker-app-uae",
    "uae-rent-bill-installment-tracker": "dubai-salary-budget",
    "expense-tracker-uae-expats": "nri-expense-tracker-uae-india",
    "free-budget-tracker-india": "best-expense-tracker-app-india",
    "upi-expense-tracker-no-manual-entry": "best-expense-tracker-app-india",
    "track-upi-card-cash-expenses": "best-expense-tracker-app-india",
    "android-bank-notification-expense-tracker": "automatic-expense-tracker-bank-sms",
    "apple-pay-expense-tracker": "automatic-expense-tracker-bank-sms",
    "private-expense-tracker-bank-alerts": "is-sms-expense-tracker-safe",
    "expense-tracker-without-bank-login": "is-sms-expense-tracker-safe",
    "sms-expense-tracker-vs-bank-sync": "is-sms-expense-tracker-safe",
    "stop-subscription-creep": "subscription-tracker-monthly-bills",
    "track-loan-repayments": "loan-tracker-money-lent",
    "income-expense-tracker": "safe-to-spend-calculator",
    "personal-cash-flow-tracker": "safe-to-spend-calculator",
    "wallet-app-alternative-private": "money-manager-alternative-automatic",
    "expense-tracker-vs-spreadsheet": "money-manager-alternative-automatic",
}
