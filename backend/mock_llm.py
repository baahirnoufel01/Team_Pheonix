import asyncio
from typing import Awaitable, Callable

from custom_types import InputMode


STREAM_CHUNK_SIZE = 5


async def mock_completion(
    process_chunk: Callable[[str], Awaitable[None]], input_mode: InputMode
) -> str:
    code_to_return = (
        GOOGLE_FORM_VIDEO_PROMPT_MOCK
        if input_mode == "video"
        else NO_IMAGES_NYTIMES_MOCK_CODE
    )

    for i in range(0, len(code_to_return), STREAM_CHUNK_SIZE):
        await process_chunk(code_to_return[i : i + STREAM_CHUNK_SIZE])
        await asyncio.sleep(0.01)

    if input_mode == "video":
        # Extract the last <html></html> block from code_to_return
        # because we can have multiple passes
        start = code_to_return.rfind("<html")
        end = code_to_return.rfind("</html>") + len("</html>")
        if start != -1 and end != -1:
            code_to_return = code_to_return[start:end]
        else:
            code_to_return = "Error: HTML block not found."

    return code_to_return


APPLE_MOCK_CODE = """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Showcase</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
        }
    </style>
</head>
<body class="bg-black text-white">
    <nav class="py-6">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center">
            <div class="flex items-center">
                <img src="https://placehold.co/24x24" alt="Company Logo" class="mr-8">
                <a href="#" class="text-white text-sm font-medium mr-4">Store</a>
                <a href="#" class="text-white text-sm font-medium mr-4">Mac</a>
                <a href="#" class="text-white text-sm font-medium mr-4">iPad</a>
                <a href="#" class="text-white text-sm font-medium mr-4">iPhone</a>
                <a href="#" class="text-white text-sm font-medium mr-4">Watch</a>
                <a href="#" class="text-white text-sm font-medium mr-4">Vision</a>
                <a href="#" class="text-white text-sm font-medium mr-4">AirPods</a>
                <a href="#" class="text-white text-sm font-medium mr-4">TV & Home</a>
                <a href="#" class="text-white text-sm font-medium mr-4">Entertainment</a>
                <a href="#" class="text-white text-sm font-medium mr-4">Accessories</a>
                <a href="#" class="text-white text-sm font-medium">Support</a>
            </div>
            <div class="flex items-center">
                <a href="#" class="text-white text-sm font-medium mr-4"><i class="fas fa-search"></i></a>
                <a href="#" class="text-white text-sm font-medium"><i class="fas fa-shopping-bag"></i></a>
            </div>
        </div>
    </nav>

    <main class="mt-8">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center">
                <img src="https://placehold.co/100x100" alt="Brand Logo" class="mx-auto mb-4">
                <h1 class="text-5xl font-bold mb-4">WATCH SERIES 9</h1>
                <p class="text-2xl font-medium mb-8">Smarter. Brighter. Mightier.</p>
                <div class="flex justify-center space-x-4">
                    <a href="#" class="text-blue-600 text-sm font-medium">Learn more ></a>
                    <a href="#" class="text-blue-600 text-sm font-medium">Buy ></a>
                </div>
            </div>
            <div class="flex justify-center mt-12">
                <img src="https://placehold.co/500x300" alt="Product image of a smartwatch with a pink band and a circular interface displaying various health metrics." class="mr-8">
                <img src="https://placehold.co/500x300" alt="Product image of a smartwatch with a blue band and a square interface showing a classic analog clock face." class="ml-8">
            </div>
        </div>
    </main>
</body>
</html>"""

NYTIMES_MOCK_CODE = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The New York Times - News</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        body {
            font-family: 'Libre Franklin', sans-serif;
        }
    </style>
</head>
<body class="bg-gray-100">
    <div class="container mx-auto px-4">
        <header class="border-b border-gray-300 py-4">
            <div class="flex justify-between items-center">
                <div class="flex items-center space-x-4">
                    <button class="text-gray-700"><i class="fas fa-bars"></i></button>
                    <button class="text-gray-700"><i class="fas fa-search"></i></button>
                    <div class="text-xs uppercase tracking-widest">Tuesday, November 14, 2023<br>Today's Paper</div>
                </div>
                <div>
                    <img src="https://placehold.co/200x50?text=The+New+York+Times+Logo" alt="The New York Times Logo" class="h-8">
                </div>
                <div class="flex items-center space-x-4">
                    <button class="bg-black text-white px-4 py-1 text-xs uppercase tracking-widest">Give the times</button>
                    <div class="text-xs">Account</div>
                </div>
            </div>
            <nav class="flex justify-between items-center py-4">
                <div class="flex space-x-4">
                    <a href="#" class="text-xs uppercase tracking-widest text-gray-700">U.S.</a>
                    <!-- Add other navigation links as needed -->
                </div>
                <div class="flex space-x-4">
                    <a href="#" class="text-xs uppercase tracking-widest text-gray-700">Cooking</a>
                    <!-- Add other navigation links as needed -->
                </div>
            </nav>
        </header>
        <main>
            <section class="py-6">
                <div class="grid grid-cols-3 gap-4">
                    <div class="col-span-2">
                        <article class="mb-4">
                            <h2 class="text-xl font-bold mb-2">Israeli Military Raids Gaza’s Largest Hospital</h2>
                            <p class="text-gray-700 mb-2">Israeli troops have entered the Al-Shifa Hospital complex, where conditions have grown dire and Israel says Hamas fighters are embedded.</p>
                            <a href="#" class="text-blue-600 text-sm">See more updates <i class="fas fa-external-link-alt"></i></a>
                        </article>
                        <!-- Repeat for each news item -->
                    </div>
                    <div class="col-span-1">
                        <article class="mb-4">
                            <img src="https://placehold.co/300x200?text=News+Image" alt="Flares and plumes of smoke over the northern Gaza skyline on Tuesday." class="mb-2">
                            <h2 class="text-xl font-bold mb-2">From Elvis to Elopements, the Evolution of the Las Vegas Wedding</h2>
                            <p class="text-gray-700 mb-2">The glittering city that attracts thousands of couples seeking unconventional nuptials has grown beyond the drive-through wedding.</p>
                            <a href="#" class="text-blue-600 text-sm">8 MIN READ</a>
                        </article>
                        <!-- Repeat for each news item -->
                    </div>
                </div>
            </section>
        </main>
    </div>
</body>
</html>
"""

NO_IMAGES_NYTIMES_MOCK_CODE = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The New York Times - News</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        body {
            font-family: 'Libre Franklin', sans-serif;
        }
    </style>
</head>
<body class="bg-gray-100">
    <div class="container mx-auto px-4">
        <header class="border-b border-gray-300 py-4">
            <div class="flex justify-between items-center">
                <div class="flex items-center space-x-4">
                    <button class="text-gray-700"><i class="fas fa-bars"></i></button>
                    <button class="text-gray-700"><i class="fas fa-search"></i></button>
                    <div class="text-xs uppercase tracking-widest">Tuesday, November 14, 2023<br>Today's Paper</div>
                </div>
                <div class="flex items-center space-x-4">
                    <button class="bg-black text-white px-4 py-1 text-xs uppercase tracking-widest">Give the times</button>
                    <div class="text-xs">Account</div>
                </div>
            </div>
            <nav class="flex justify-between items-center py-4">
                <div class="flex space-x-4">
                    <a href="#" class="text-xs uppercase tracking-widest text-gray-700">U.S.</a>
                    <!-- Add other navigation links as needed -->
                </div>
                <div class="flex space-x-4">
                    <a href="#" class="text-xs uppercase tracking-widest text-gray-700">Cooking</a>
                    <!-- Add other navigation links as needed -->
                </div>
            </nav>
        </header>
        <main>
            <section class="py-6">
                <div class="grid grid-cols-3 gap-4">
                    <div class="col-span-2">
                        <article class="mb-4">
                            <h2 class="text-xl font-bold mb-2">Israeli Military Raids Gaza’s Largest Hospital</h2>
                            <p class="text-gray-700 mb-2">Israeli troops have entered the Al-Shifa Hospital complex, where conditions have grown dire and Israel says Hamas fighters are embedded.</p>
                            <a href="#" class="text-blue-600 text-sm">See more updates <i class="fas fa-external-link-alt"></i></a>
                        </article>
                        <!-- Repeat for each news item -->
                    </div>
                    <div class="col-span-1">
                        <article class="mb-4">
                            <h2 class="text-xl font-bold mb-2">From Elvis to Elopements, the Evolution of the Las Vegas Wedding</h2>
                            <p class="text-gray-700 mb-2">The glittering city that attracts thousands of couples seeking unconventional nuptials has grown beyond the drive-through wedding.</p>
                            <a href="#" class="text-blue-600 text-sm">8 MIN READ</a>
                        </article>
                        <!-- Repeat for each news item -->
                    </div>
                </div>
            </section>
        </main>
    </div>
</body>
</html>
"""

MORTGAGE_CALCULATOR_VIDEO_PROMPT_MOCK = """
<thinking>
The user flow in the video seems to be:
1. The calculator starts with some default values for loan amount, loan term, interest rate, etc. 
2. The user toggles the "Include taxes & fees" checkbox which shows an explanation tooltip.
3. The user selects different loan terms from the dropdown, which updates the monthly payment amount.
4. The user enters a custom loan amount.
5. The user selects a different loan term (30-yr fixed FHA).
6. The user enters additional details like home price, down payment, state, credit score, property tax, home insurance, and HOA fees.
7. The calculator updates the total monthly payment breakdown.

To build this:
- Use a container div for the whole calculator
- Have sections for Monthly Payment, Purchase Budget, loan details, additional costs
- Use input fields, dropdowns, and checkboxes for user input
- Update values dynamically using JavaScript when inputs change
- Show/hide explanation tooltip when checkbox is toggled
- Update monthly payment whenever loan amount, interest rate or term is changed
- Allow selecting loan term from a dropdown 
- Update total monthly payment breakdown as additional costs are entered
- Style everything to match the screenshots using Tailwind utility classes
</thinking>

<html>
<head>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>
<body>
<div class="max-w-lg mx-auto bg-white shadow-lg rounded-lg p-6 font-sans">
  <div class="text-2xl font-semibold mb-6">Mortgage Calculator</div>
  
  <div class="flex justify-between text-sm uppercase font-semibold text-gray-500 border-b mb-4">
    <div class="pb-2 border-b-2 border-blue-500">Monthly payment</div>
    <div class="pb-2">Purchase budget</div>
  </div>

  <div class="flex items-center mb-4">
    <input type="checkbox" class="mr-2 taxes-toggle" id="taxesToggle">
    <label for="taxesToggle" class="text-sm">Include taxes & fees</label>
    <i class="fas fa-info-circle ml-1 text-gray-400 cursor-pointer" id="taxesInfo"></i>
    <div class="hidden bg-gray-100 text-xs p-2 ml-2 rounded" id="taxesTooltip">Your total monthly payment is more than just your mortgage. It can include property taxes, homeowners insurance, and HOA fees, among other things.</div>
  </div>

  <div class="text-3xl font-semibold mb-4">$<span id="monthlyPayment">1,696</span></div>

  <div class="mb-4">
    <div class="text-sm font-semibold mb-2">Loan amount</div>
    <input type="text" value="240,000" class="w-full border rounded px-2 py-1 text-lg" id="loanAmount">
  </div>

  <div class="mb-4">
    <div class="text-sm font-semibold mb-2">Loan term</div>
    <select class="w-full border rounded px-2 py-1 text-lg" id="loanTerm">
      <option>30-yr fixed</option>
      <option>30-yr fixed FHA</option>
      <option>30-yr fixed VA</option>
      <option>30-yr fixed USDA</option>
      <option>20-yr fixed</option>
      <option>15-yr fixed</option>
      <option>10 / 6 ARM</option>
      <option>7 / 6 ARM</option>
      <option>5 / 6 ARM</option>
      <option>3 / 6 ARM</option>
    </select>
  </div>

  <div class="flex justify-between mb-4">
    <div>
      <div class="text-sm font-semibold mb-2">Interest</div>
      <div class="text-lg">7.61 %</div>
    </div>
    <i class="fas fa-info-circle text-gray-400 cursor-pointer self-center"></i>
  </div>

  <div class="border-t pt-4">
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Home price</div>
      <input type="text" value="300,000" class="w-full border rounded px-2 py-1 text-lg" id="homePrice">
    </div>
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Down payment</div>
      <div class="flex">
        <input type="text" value="60,000" class="w-full border rounded-l px-2 py-1 text-lg" id="downPayment">
        <div class="bg-gray-200 rounded-r px-4 py-1 text-lg flex items-center">20 %</div>
      </div>
    </div>
  </div>

  <div class="border-t pt-4">
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">State</div>
      <select class="w-full border rounded px-2 py-1 text-lg" id="state">
        <option>New York</option>
      </select>
    </div>
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Credit score</div>
      <select class="w-full border rounded px-2 py-1 text-lg" id="creditScore">
        <option>700 - 719</option>
      </select>
    </div>
  </div>

  <div class="border-t pt-4">
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Property tax (yearly)</div>
      <input type="text" value="3,750" class="w-full border rounded px-2 py-1 text-lg" id="propertyTax">
    </div>
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Home insurance (yearly)</div>
      <input type="text" value="1,050" class="w-full border rounded px-2 py-1 text-lg" id="homeInsurance">
    </div>
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Private mortgage insurance (monthly)</div>
      <input type="text" value="0" class="w-full border rounded px-2 py-1 text-lg" id="mortgageInsurance">
    </div>
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Homeowners association (monthly)</div>
      <input type="text" value="0" class="w-full border rounded px-2 py-1 text-lg" id="hoaFees">
    </div>
  </div>

  <div class="flex justify-between pt-4">
    <div class="text-sm">
      <div class="font-semibold">Total monthly payment</div>
      <div class="text-3xl font-semibold">$<span id="totalPayment">2,036</span></div>
    </div>
    <div class="text-right">
      <div class="text-sm">Loan</div>
      <div class="text-lg">$<span id="loanPayment">1,635</span></div>
      <div class="text-sm">Taxes & fees</div>
      <div>$<span id="taxesPayment">401</span></div>
    </div>
  </div>

  <div class="text-xs text-gray-500 mt-4">
    <div>Disclaimer • Feedback</div>
  </div>
</div>

<script>
$(document).ready(function() {
  var loanAmount = 240000;
  var interestRate = 7.61;
  var loanTerm = 30;
  var homePrice = 300000;
  var downPayment = 60000;
  var propertyTax = 3750;
  var homeInsurance = 1050;
  var mortgageInsurance = 0;
  var hoaFees = 0;

  function updateCalculations() {
    var principal = loanAmount;
    var monthlyInterest = interestRate / 100 / 12;
    var numPayments = loanTerm * 12;
    var monthlyPayment = principal * monthlyInterest / (1 - (Math.pow(1/(1 + monthlyInterest), numPayments)));
    var totalPayment = monthlyPayment;
    var taxesPayment = (propertyTax + homeInsurance) / 12;

    if ($('#taxesToggle').is(':checked')) {
      totalPayment += taxesPayment + mortgageInsurance + hoaFees;
    }

    $('#monthlyPayment').text(Math.round(monthlyPayment).toLocaleString());
    $('#loanPayment').text(Math.round(monthlyPayment).toLocaleString());
    $('#taxesPayment').text(Math.round(taxesPayment + mortgageInsurance + hoaFees).toLocaleString());
    $('#totalPayment').text(Math.round(totalPayment).toLocaleString());
  }

  $('#taxesInfo').hover(function() {
    $('#taxesTooltip').removeClass('hidden');
  }, function() {
    $('#taxesTooltip').addClass('hidden');
  });

  $('#loanTerm').change(function() {
    loanTerm = parseInt($(this).val().split('-')[0]);
    updateCalculations();
  });

  $('#loanAmount').change(function() {
    loanAmount = parseInt($(this).val().replace(/,/g, ''));
    updateCalculations();
  });

  $('#homePrice').change(function() {
    homePrice = parseInt($(this).val().replace(/,/g, ''));
    loanAmount = homePrice - downPayment;
    $('#loanAmount').val(loanAmount.toLocaleString());
    updateCalculations();
  });

  $('#downPayment').change(function() {
    downPayment = parseInt($(this).val().replace(/,/g, ''));
    loanAmount = homePrice - downPayment;
    $('#loanAmount').val(loanAmount.toLocaleString());
    updateCalculations();
  });

  $('#propertyTax').change(function() {
    propertyTax = parseInt($(this).val().replace(/,/g, ''));
    updateCalculations();
  });

  $('#homeInsurance').change(function() {
    homeInsurance = parseInt($(this).val().replace(/,/g, ''));
    updateCalculations();
  });

  $('#mortgageInsurance').change(function() {
    mortgageInsurance = parseInt($(this).val().replace(/,/g, ''));
    updateCalculations();
  });

  $('#hoaFees').change(function() {
    hoaFees = parseInt($(this).val().replace(/,/g, ''));
    updateCalculations();
  });

  updateCalculations();
});
</script>
</body>
</html>

<thinking>
More things to consider:
- Add validation to input fields to prevent non-numeric values
- Add a reset button to clear all inputs and reset to default values
</thinking>

<html>
<head>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>
<body>
<div class="max-w-lg mx-auto bg-black text-white shadow-lg rounded-lg p-6 font-sans">
  <div class="text-2xl font-semibold mb-6">Mortgage Calculator</div>
  
  <div class="flex justify-between text-sm uppercase font-semibold text-gray-500 border-b mb-4">
    <div class="pb-2 border-b-2 border-blue-500">Monthly payment</div>
    <div class="pb-2">Purchase budget</div>
  </div>

  <div class="flex items-center mb-4">
    <input type="checkbox" class="mr-2 taxes-toggle" id="taxesToggle">
    <label for="taxesToggle" class="text-sm">Include taxes & fees</label>
    <i class="fas fa-info-circle ml-1 text-gray-400 cursor-pointer" id="taxesInfo"></i>
    <div class="hidden bg-gray-100 text-xs p-2 ml-2 rounded" id="taxesTooltip">Your total monthly payment is more than just your mortgage. It can include property taxes, homeowners insurance, and HOA fees, among other things.</div>
  </div>

  <div class="text-3xl font-semibold mb-4">$<span id="monthlyPayment">1,696</span></div>

  <div class="mb-4">
    <div class="text-sm font-semibold mb-2">Loan amount</div>
    <input type="text" value="240,000" class="w-full border rounded px-2 py-1 text-lg" id="loanAmount">
  </div>

  <div class="mb-4">
    <div class="text-sm font-semibold mb-2">Loan term</div>
    <select class="w-full border rounded px-2 py-1 text-lg" id="loanTerm">
      <option>30-yr fixed</option>
      <option>30-yr fixed FHA</option>
      <option>30-yr fixed VA</option>
      <option>30-yr fixed USDA</option>
      <option>20-yr fixed</option>
      <option>15-yr fixed</option>
      <option>10 / 6 ARM</option>
      <option>7 / 6 ARM</option>
      <option>5 / 6 ARM</option>
      <option>3 / 6 ARM</option>
    </select>
  </div>

  <div class="flex justify-between mb-4">
    <div>
      <div class="text-sm font-semibold mb-2">Interest</div>
      <div class="text-lg">7.61 %</div>
    </div>
    <i class="fas fa-info-circle text-gray-400 cursor-pointer self-center"></i>
  </div>

  <div class="border-t pt-4">
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Home price</div>
      <input type="text" value="300,000" class="w-full border rounded px-2 py-1 text-lg" id="homePrice">
    </div>
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Down payment</div>
      <div class="flex">
        <input type="text" value="60,000" class="w-full border rounded-l px-2 py-1 text-lg" id="downPayment">
        <div class="bg-gray-200 rounded-r px-4 py-1 text-lg flex items-center">20 %</div>
      </div>
    </div>
  </div>

  <div class="border-t pt-4">
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">State</div>
      <select class="w-full border rounded px-2 py-1 text-lg" id="state">
        <option>New York</option>
      </select>
    </div>
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Credit score</div>
      <select class="w-full border rounded px-2 py-1 text-lg" id="creditScore">
        <option>700 - 719</option>
      </select>
    </div>
  </div>

  <div class="border-t pt-4">
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Property tax (yearly)</div>
      <input type="text" value="3,750" class="w-full border rounded px-2 py-1 text-lg" id="propertyTax">
    </div>
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Home insurance (yearly)</div>
      <input type="text" value="1,050" class="w-full border rounded px-2 py-1 text-lg" id="homeInsurance">
    </div>
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Private mortgage insurance (monthly)</div>
      <input type="text" value="0" class="w-full border rounded px-2 py-1 text-lg" id="mortgageInsurance">
    </div>
    <div class="mb-4">
      <div class="text-sm font-semibold mb-2">Homeowners association (monthly)</div>
      <input type="text" value="0" class="w-full border rounded px-2 py-1 text-lg" id="hoaFees">
    </div>
  </div>

  <div class="flex justify-between pt-4">
    <div class="text-sm">
      <div class="font-semibold">Total monthly payment</div>
      <div class="text-3xl font-semibold">$<span id="totalPayment">2,036</span></div>
    </div>
    <div class="text-right">
      <div class="text-sm">Loan</div>
      <div class="text-lg">$<span id="loanPayment">1,635</span></div>
      <div class="text-sm">Taxes & fees</div>
      <div>$<span id="taxesPayment">401</span></div>
    </div>
  </div>

  <div class="text-xs text-gray-500 mt-4">
    <div>Disclaimer • Feedback</div>
  </div>
</div>

<script>
$(document).ready(function() {
  var loanAmount = 240000;
  var interestRate = 7.61;
  var loanTerm = 30;
  var homePrice = 300000;
  var downPayment = 60000;
  var propertyTax = 3750;
  var homeInsurance = 1050;
  var mortgageInsurance = 0;
  var hoaFees = 0;

  function updateCalculations() {
    var principal = loanAmount;
    var monthlyInterest = interestRate / 100 / 12;
    var numPayments = loanTerm * 12;
    var monthlyPayment = principal * monthlyInterest / (1 - (Math.pow(1/(1 + monthlyInterest), numPayments)));
    var totalPayment = monthlyPayment;
    var taxesPayment = (propertyTax + homeInsurance) / 12;

    if ($('#taxesToggle').is(':checked')) {
      totalPayment += taxesPayment + mortgageInsurance + hoaFees;
    }

    $('#monthlyPayment').text(Math.round(monthlyPayment).toLocaleString());
    $('#loanPayment').text(Math.round(monthlyPayment).toLocaleString());
    $('#taxesPayment').text(Math.round(taxesPayment + mortgageInsurance + hoaFees).toLocaleString());
    $('#totalPayment').text(Math.round(totalPayment).toLocaleString());
  }

  $('#taxesInfo').hover(function() {
    $('#taxesTooltip').removeClass('hidden');
  }, function() {
    $('#taxesTooltip').addClass('hidden');
  });

  $('#loanTerm').change(function() {
    loanTerm = parseInt($(this).val().split('-')[0]);
    updateCalculations();
  });

  $('#loanAmount').change(function() {
    loanAmount = parseInt($(this).val().replace(/,/g, ''));
    updateCalculations();
  });

  $('#homePrice').change(function() {
    homePrice = parseInt($(this).val().replace(/,/g, ''));
    loanAmount = homePrice - downPayment;
    $('#loanAmount').val(loanAmount.toLocaleString());
    updateCalculations();
  });

  $('#downPayment').change(function() {
    downPayment = parseInt($(this).val().replace(/,/g, ''));
    loanAmount = homePrice - downPayment;
    $('#loanAmount').val(loanAmount.toLocaleString());
    updateCalculations();
  });

  $('#propertyTax').change(function() {
    propertyTax = parseInt($(this).val().replace(/,/g, ''));
    updateCalculations();
  });

  $('#homeInsurance').change(function() {
    homeInsurance = parseInt($(this).val().replace(/,/g, ''));
    updateCalculations();
  });

  $('#mortgageInsurance').change(function() {
    mortgageInsurance = parseInt($(this).val().replace(/,/g, ''));
    updateCalculations();
  });

  $('#hoaFees').change(function() {
    hoaFees = parseInt($(this).val().replace(/,/g, ''));
    updateCalculations();
  });

  updateCalculations();
});
</script>
</body>
</html>

"""

GOOGLE_FORM_VIDEO_PROMPT_MOCK = """
<thinking>
To build this:
- Create a search bar that allows typing and shows placeholder text
- Implement search suggestions that update as the user types
- Allow selecting a suggestion to perform that search
- Show search results with the query and an AI-powered overview 
- Have filter tabs for different search verticals 
- Allow clicking filter tabs to add/remove them, updating the URL
- Ensure the UI closely matches the Google style and colors
</thinking>

<html>
<head>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
  <style>
    body {
      font-family: Arial, sans-serif;
    }
    .filter {
      color: #1a73e8;
    }
    .filter.active {
      background-color: #e2eeff;
      border-bottom: 3px solid #1a73e8;
    }
  </style>
</head>
<body>

<div class="flex justify-end items-center p-4 text-sm text-gray-700">
  <div class="mr-4">Gmail</div>
  <div class="mr-4">Images</div>
  <img class="h-8 w-8 rounded-full" src="https://via.placeholder.com/150" alt="User avatar">
</div>

<div class="flex flex-col items-center mt-44">
  <img class="w-72" src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="Google logo">
  
  <div class="relative mt-8 w-full max-w-xl">
    <input id="search" type="text" class="w-full px-4 py-3 text-lg rounded-full border border-gray-200 hover:shadow-lg focus:outline-none focus:shadow-lg" placeholder="Google Search">
    <i class="absolute right-0 top-0 m-3 text-blue-500 text-xl fas fa-microphone"></i>
  </div>

  <div id="suggestions" class="flex flex-col w-full max-w-xl border border-gray-100 shadow-lg mt-1 rounded-lg hidden">
  </div>

  <div class="flex justify-center space-x-4 mt-8">
    <button class="px-6 py-3 bg-gray-100 text-gray-800 rounded-md hover:shadow-md focus:outline-none">Google Search</button>
    <button class="px-6 py-3 bg-gray-100 text-gray-800 rounded-md hover:shadow-md focus:outline-none">I'm Feeling Lucky</button>
  </div>
</div>

<div id="results" class="mt-8 hidden">
  <div class="flex justify-between items-center px-5 py-3 text-sm">
    <div>
      <span class="text-blue-600 mr-3 filter active" data-filter="all">All</span>
      <span class="text-blue-600 mr-3 filter" data-filter="news">News</span>
      <span class="text-blue-600 mr-3 filter" data-filter="images">Images</span>
      <span class="text-blue-600 mr-3 filter" data-filter="videos">Videos</span>
      <span class="text-blue-600 mr-3 filter" data-filter="shopping">Shopping</span>
      <span class="text-blue-600 mr-3 filter" data-filter="maps">Maps</span>
      <span class="text-blue-600 mr-3 filter" data-filter="books">Books</span>
      <span class="text-blue-600 mr-3 filter" data-filter="flights">Flights</span>
      <span class="text-blue-600 mr-3 filter" data-filter="finance">Finance</span>
    </div>
    <div>
      <span class="text-gray-600">Settings</span>
      <span class="text-gray-600 ml-3">Tools</span>
      <span class="text-gray-600 ml-3">SafeSearch</span>
    </div>
  </div>

  <div class="px-5 py-3">
    <div class="text-sm text-gray-600">Results for <span id="location">New York, NY 10022</span> - Choose area</div>
    <button id="overview" class="px-4 py-2 mt-2 text-white bg-blue-500 rounded-md">Get an AI-powered overview for this search</button>
  </div>

  <div id="overview-text" class="px-5 py-3"></div>

  <div class="px-5 py-3">
    <div class="text-xl text-blue-600">The New York Times</div>
    <div class="text-sm text-green-700">https://www.nytimes.com</div>
    <div class="mt-2">The New York Times - Breaking News, US News, World News ...</div>
    <div class="text-sm text-gray-600">Live news, investigations, opinion, photos and video by the journalists of The New York Times from more than 150 countries around the world.</div>
  </div>
</div>

<script>
const searchSuggestions = {
  "t": ["times", "translate", "twitter", "target"],
  "ti": ["times", "times square", "tiktok", "tires"],
  "tim": ["times", "times square", "time", "timer"],
  "time": ["times", "times square", "time", "time magazine"],
  "times": ["times", "times square", "times table", "times of india"]
};

let currentSearch = '';

$('#search').on('input', function() {
  currentSearch = $(this).val().trim().toLowerCase();

  if (currentSearch.length > 0) {
    const suggestions = searchSuggestions[currentSearch] || [];
    const suggestionsHtml = suggestions.map(s => `<div class="px-4 py-2 hover:bg-gray-100 cursor-pointer">${s}</div>`).join('');
    $('#suggestions').html(suggestionsHtml).show();
  } else {
    $('#suggestions').empty().hide();
  }
});

$('#suggestions').on('click', 'div', function() {
  const suggestion = $(this).text();
  $('#search').val(suggestion);
  $('#suggestions').empty().hide();
  performSearch(suggestion);
});

$('#search').on('keypress', function(e) {
  if (e.which === 13) {
    const query = $(this).val();
    performSearch(query);
  }
});

function performSearch(query) {
  $('#results').show();
  $('.filter').removeClass('active');
  $('.filter[data-filter="all"]').addClass('active');
  updateFilters('all');
  $('#overview-text').empty();
}

$('.filter').on('click', function() {
  $('.filter').removeClass('active');
  $(this).addClass('active');
  const filter = $(this).data('filter');
  updateFilters(filter);
});

function updateFilters(activeFilter) {
  const filters = ['all', 'news', 'images', 'videos', 'shopping', 'maps', 'books', 'flights', 'finance'];
  let filtersHtml = '';

  filters.forEach(filter => {
    if (filter === activeFilter) {
      filtersHtml += `<span class="text-blue-600 mr-3 filter active" data-filter="${filter}">${filter.charAt(0).toUpperCase() + filter.slice(1)}</span>`;
    } else if (filters.indexOf(filter) <= filters.indexOf(activeFilter)) {
      filtersHtml += `<span class="text-blue-600 mr-3 filter" data-filter="${filter}">${filter.charAt(0).toUpperCase() + filter.slice(1)}</span>`;
    }
  });

  $('.flex.justify-between').find('div:first-child').html(filtersHtml);
  window.history.pushState({}, '', `?q=${encodeURIComponent(currentSearch)}&filter=${activeFilter}`);
}

$('#overview').on('click', function() {
  $('#overview-text').text('Try AI-powered overviews when you search');
});
</script>
</body>
</html>

<thinking>To further improve the app based on the original instructions:

1. Adjust the font sizes, colors, and spacing to more closely match the Google style.
2. Add the hover effect on the search bar to expand its shadow.
3. Position the microphone icon correctly inside the search bar.
4. Implement the "I'm Feeling Lucky" functionality to redirect to the first search result.
5. Add the "Search by voice" and "Search by image" options that appear on hover.
6. Show the "Clear" button in the search bar when there's text entered.
7. Make the search suggestions clickable to perform the search.
8. Update the page title and URL when a search is performed.
9. Show a more realistic search result with a link, description, and URL.
10. Add more filter options and make them functional to update the search results.
11. Generate a more realistic AI-powered overview of the search topic.
12. Refine the responsive layout for different screen sizes.
</thinking>

<html>
<head>
  <title>Google</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Roboto', Arial, sans-serif;
      font-size: 14px;
      color: #202124;
    }
    .filter {
      color: #1a73e8;
    }
    .filter.active {
      border-bottom: 3px solid #1a73e8;
    }
    .search-bar:hover {
      box-shadow: 0 1px 6px rgb(32 33 36 / 28%);
      border-color: rgba(223,225,229,0);
    }
    .search-bar:focus-within {
      box-shadow: 0 1px 6px rgb(32 33 36 / 28%);
      border-color: rgba(223,225,229,0);
    }
  </style>
</head>
<body>

<div class="flex justify-end items-center p-2 text-sm">
  <div class="mr-4 hover:underline cursor-pointer">Gmail</div>
  <div class="mr-4 hover:underline cursor-pointer">Images</div>
  <img class="h-8 w-8 rounded-full" src="https://via.placeholder.com/150" alt="User avatar">
</div>

<div class="flex flex-col items-center mt-40">
  <img class="w-72" src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="Google logo">
  
  <div class="relative mt-6 w-full max-w-[584px]">
    <input id="search" type="text" class="w-full px-5 py-3 text-base rounded-full border border-gray-200 hover:shadow-lg focus:outline-none focus:shadow-lg search-bar" placeholder="Google Search" autocomplete="off">
    <i class="absolute right-0 top-0 m-3.5 text-[#4285f4] text-xl fas fa-microphone"></i>
    <i id="clear-search" class="absolute right-0 top-0 m-3.5 text-gray-500 text-2xl fas fa-times cursor-pointer hidden"></i>
  </div>

  <div id="search-options" class="flex justify-center space-x-2 mt-2 text-sm text-[#4285f4] hidden">
    <div class="flex items-center cursor-pointer">
      <i class="fas fa-search mr-1"></i>
      <span>Search by voice</span>
    </div>
    <div class="flex items-center cursor-pointer">
      <i class="fas fa-camera mr-1"></i>
      <span>Search by image</span>
    </div>
  </div>

  <div id="suggestions" class="flex flex-col w-full max-w-[584px] border border-gray-100 shadow-lg rounded-lg bg-white hidden">
  </div>

  <div class="flex justify-center space-x-4 mt-8">
    <button id="search-button" class="px-6 py-2 bg-[#f8f9fa] text-[#3c4043] rounded text-sm hover:shadow-md focus:outline-none">Google Search</button>
    <button id="lucky-button" class="px-6 py-2 bg-[#f8f9fa] text-[#3c4043] rounded text-sm hover:shadow-md focus:outline-none">I'm Feeling Lucky</button>
  </div>
</div>

<div id="results" class="mt-6 hidden">
  <div class="flex justify-between items-center px-4 py-2.5 text-sm">
    <div>
      <span class="text-[#4285f4] mr-3 filter active" data-filter="all">All</span>
      <span class="text-[#4285f4] mr-3 filter" data-filter="news">News</span>
      <span class="text-[#4285f4] mr-3 filter" data-filter="images">Images</span>
      <span class="text-[#4285f4] mr-3 filter" data-filter="videos">Videos</span>
      <span class="text-[#4285f4] mr-3 filter" data-filter="shopping">Shopping</span>
      <span class="text-[#4285f4] mr-3 filter" data-filter="maps">Maps</span>
      <span class="text-[#4285f4] mr-3 filter" data-filter="books">Books</span>
      <span class="text-[#4285f4] mr-3 filter" data-filter="flights">Flights</span>
      <span class="text-[#4285f4] mr-3 filter" data-filter="finance">Finance</span>
    </div>
    <div>
      <span class="text-[#70757a] hover:underline cursor-pointer">Settings</span>
      <span class="text-[#70757a] ml-6 hover:underline cursor-pointer">Tools</span>
      <span class="text-[#70757a] ml-6 hover:underline cursor-pointer">SafeSearch</span>
    </div>
  </div>

  <div class="px-4 py-3">
    <div class="text-[#70757a]">Results for <span id="location">New York, NY 10022</span> - <span class="hover:underline cursor-pointer">Choose area</span></div>
    <button id="overview" class="px-4 py-2.5 mt-2 text-white bg-[#1a73e8] rounded text-sm hover:bg-[#1a65c7]">Get an AI-powered overview for this search</button>
  </div>

  <div id="overview-text" class="px-4 py-3 text-sm"></div>

  <div class="px-4 py-3">
    <div class="text-xl text-[#1a0dab] hover:underline cursor-pointer">The New York Times</div>
    <div class="text-sm text-[#006621] hover:underline cursor-pointer">https://www.nytimes.com</div>
    <div class="mt-1">The New York Times - Breaking News, US News, World News ...</div>
    <div class="text-sm text-[#545454]">Live news, investigations, opinion, photos and video by the journalists of The New York Times from more than 150 countries around the world.</div>
  </div>
</div>

<script>
const searchSuggestions = {
  "t": ["times", "translate", "twitter", "target"],
  "ti": ["times", "times square", "tiktok", "tires"],
  "tim": ["times", "times square", "time", "timer"],
  "time": ["times", "times square", "time", "time magazine"],
  "times": ["times", "times square", "times table", "times of india"]
};

let currentSearch = '';

$('#search').on('input', function() {
  currentSearch = $(this).val().trim().toLowerCase();

  if (currentSearch.length > 0) {
    const suggestions = searchSuggestions[currentSearch] || [];
    const suggestionsHtml = suggestions.map(s => `<div class="px-4 py-2 hover:bg-gray-100 cursor-pointer">${s}</div>`).join('');
    $('#suggestions').html(suggestionsHtml).show();
    $('#clear-search').show();
    $('#search-options').hide();
  } else {
    $('#suggestions').empty().hide();
    $('#clear-search').hide();
    $('#search-options').show();
  }
});

$('#suggestions').on('click', 'div', function() {
  const suggestion = $(this).text();
  $('#search').val(suggestion);
  $('#suggestions').empty().hide();
  performSearch(suggestion);
});

$('#search').on('keypress', function(e) {
  if (e.which === 13) {
    const query = $(this).val();
    performSearch(query);
  }
});

$('#search-button').on('click', function() {
  const query = $('#search').val();
  performSearch(query);
});

$('#lucky-button').on('click', function() {
  window.location.href = 'https://www.google.com/doodles';
});

$('#clear-search').on('click', function() {
  $('#search').val('');
  $('#suggestions').empty().hide();
  $(this).hide();
  $('#search-options').show();
  $('#search').focus();
});

$('#search').on('focus', function() {
  if ($(this).val().length > 0) {
    $('#search-options').hide();
  } else {
    $('#search-options').show();
  }
});

$('#search').on('blur', function() {
  $('#search-options').hide();
});

function performSearch(query) {
  $('#results').show();
  $('.filter').removeClass('active');
  $('.filter[data-filter="all"]').addClass('active');
  updateFilters('all');
  $('#overview-text').empty();
  window.history.pushState({}, '', `?q=${encodeURIComponent(query)}`);
  document.title = `${query} - Google Search`;
}

$('.filter').on('click', function() {
  $('.filter').removeClass('active');
  $(this).addClass('active');
  const filter = $(this).data('filter');
  updateFilters(filter);
});

function updateFilters(activeFilter) {
  const filters = ['all', 'news', 'images', 'videos', 'shopping', 'maps', 'books', 'flights', 'finance'];
  let filtersHtml = '';

  filters.forEach(filter => {
    if (filter === activeFilter) {
      filtersHtml += `<span class="text-[#4285f4] mr-3 filter active" data-filter="${filter}">${filter.charAt(0).toUpperCase() + filter.slice(1)}</span>`;
    } else if (filters.indexOf(filter) <= filters.indexOf(activeFilter)) {
      filtersHtml += `<span class="text-[#4285f4] mr-3 filter" data-filter="${filter}">${filter.charAt(0).toUpperCase() + filter.slice(1)}</span>`;
    }
  });

  $('.flex.justify-between').find('div:first-child').html(filtersHtml);
  window.history.pushState({}, '', `?q=${encodeURIComponent(currentSearch)}&filter=${activeFilter}`);
}

$('#overview').on('click', function() {
  $('#overview-text').text('Try AI-powered overviews when you search. These provide a quick understanding of topics based on information from across the web.');
});
</script>

</body>
</html>
"""

TALLY_FORM_VIDEO_PROMPT_MOCK = """
<thinking>
The user flow in the video seems to be:
1. The quiz starts by asking "What is the capital of Bulgaria?" with three multiple choice options. The user selects "Sofia".
2. The next question asks "What is the most famous dish in Belgium?" with two image-based options. The user selects "Steak with fries".
3. The next question asks "What is the name of this actor?" with an image of an older man with gray hair and beard. The user types in "Clooney" and submits the answer.
4. The quiz ends showing the user's score of 10/30 and a "Bummer, try again!" message with an arrow to restart.

To build this as a functional web app:
1. Create the overall page structure with a title, question area, answer options area, and next/submit buttons.
2. Use jQuery to show/hide different questions and update the answer options based on the current question. 
3. Store the questions, answer options, and correct answers in a Javascript array.
4. Keep track of the user's selections and compare them to the correct answers to calculate the score.
5. After the last question, show the final score and restart option.
6. Style everything to match the screenshots using Tailwind utility classes.
</thinking>

<html>
<!DOCTYPE html>
<html>
<head>
  <title>Online Trivia Quiz</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
</head>
<body class="bg-white text-gray-800 p-6">
  <h1 class="text-2xl font-bold mb-4">Online Trivia Quiz</h1>
  
  <div id="question-container" class="mb-6">
    <h2 id="question" class="text-xl mb-4"></h2>
    <div id="options" class="space-y-4"></div>
  </div>
  
  <div id="actor-container" class="mb-6 hidden">
    <img id="actor-image" src="" alt="" class="mb-4 w-2/3 mx-auto rounded-lg">
    <input type="text" id="actor-answer" class="border rounded w-full py-2 px-3 text-gray-700 mb-3">
  </div>

  <div id="result-container" class="text-center hidden">
    <h2 class="text-xl mb-2">Bummer, try again!</h2>
    <p id="score" class="text-lg mb-4"></p>
    <button id="restart-btn" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
      <i class="fas fa-redo mr-2"></i> Restart
    </button>
  </div>

  <button id="next-btn" class="bg-black hover:bg-gray-800 text-white font-bold py-2 px-4 rounded">
    Next <i class="fas fa-arrow-right ml-2"></i>
  </button>
  
  <button id="submit-btn" class="bg-black hover:bg-gray-800 text-white font-bold py-2 px-4 rounded hidden">
    Submit <i class="fas fa-arrow-right ml-2"></i>
  </button>

  <script>
    const quizData = [
      {
        question: "What is the capital of Bulgaria?",
        options: ["Sofia", "Plovdiv", "Varna"],
        answer: "Sofia"
      },
      {
        question: "What is the most famous dish in Belgium?", 
        options: [
          {
            image: "https://via.placeholder.com/300x200?text=Spaghetti",
            alt: "A bowl of spaghetti pasta with tomato sauce and parmesan cheese on top",
            text: "Spaghetti"
          },
          {
            image: "https://via.placeholder.com/300x200?text=Steak+with+fries",
            alt: "A plate with grilled steak, french fries, and greens",
            text: "Steak with fries"
          }
        ],
        answer: "Steak with fries"
      },
      {
        question: "What is the name of this actor?",
        image: "https://via.placeholder.com/400x300?text=Older+man+with+gray+hair+and+beard",
        alt: "Headshot of an older man with gray hair and a gray beard wearing a black suit and bowtie",
        answer: "Clooney"
      }
    ];

    let currentQuestion = 0;
    let score = 0;

    function startQuiz() {
      currentQuestion = 0;
      score = 0;
      $("#question-container").show();
      $("#actor-container").hide();
      $("#result-container").hide();
      $("#next-btn").show();
      $("#submit-btn").hide();
      showQuestion();
    }

    function showQuestion() {
      const questionData = quizData[currentQuestion];
      $("#question").text(questionData.question);
      
      if (questionData.options) {
        let optionsHtml = "";
        for (let option of questionData.options) {
          if (typeof option === "string") {
            optionsHtml += `
              <div>
                <label>
                  <input type="radio" name="answer" value="${option}">
                  ${option}
                </label>
              </div>
            `;
          } else {
            optionsHtml += `
              <div>
                <label>
                  <input type="radio" name="answer" value="${option.text}">
                  <img src="${option.image}" alt="${option.alt}" class="w-full mb-2">
                  ${option.text}
                </label>
              </div>
            `;
          }
        }
        $("#options").html(optionsHtml);
        $("#actor-container").hide();
      } else {
        $("#options").empty();
        $("#actor-image").attr("src", questionData.image).attr("alt", questionData.alt);
        $("#actor-answer").val("");
        $("#actor-container").show();
        $("#next-btn").hide();
        $("#submit-btn").show();
      }
    }

    function checkAnswer() {
      const questionData = quizData[currentQuestion];
      
      let userAnswer;
      if (questionData.options) {
        userAnswer = $("input[name='answer']:checked").val();
      } else {
        userAnswer = $("#actor-answer").val().trim();
      }

      if (userAnswer === questionData.answer) {
        score++;
      }

      currentQuestion++;
      
      if (currentQuestion < quizData.length) {
        showQuestion();
      } else {
        showResult();
      }
    }

    function showResult() {
      $("#question-container").hide();
      $("#actor-container").hide();
      $("#score").text(`Your score is: ${score} / ${quizData.length}`);
      $("#result-container").show();
    }

    $("#next-btn").click(checkAnswer);
    $("#submit-btn").click(checkAnswer);
    $("#restart-btn").click(startQuiz);

    startQuiz();
  </script>
</body>
</html>
</html>

This implements the online trivia quiz app as shown in the video. It uses jQuery to handle the interactions and Tailwind CSS for styling. The questions, options, and answers are defined in the quizData array. The app keeps track of the user's current question and score, allows selecting or entering answers, and displays the final score at the end with the option to restart.

<thinking>
To further improve the app to match the original video:

1. Adjust the styling to more closely match the font, colors, spacing, and layout in the screenshots. 
2. Add a cursor pointer when hovering over answer options.
3. Improve the styling of the selected answer option.
4. Make the "Next" button change to an arrow icon on hover.
5. Add a "Back" button to go to the previous question.
6. Show the current question number and total (e.g. "Question 1 of 3").
7. Animate the transitions between questions.
8. Improve the responsive layout for different screen sizes.
9. Preload the images to avoid flickering.
10. Refactor the code to be more modular and maintainable.
</thinking>

<html>
<!DOCTYPE html>
<html>
<head>
  <title>Online Trivia Quiz</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
    body {
      font-family: 'Roboto', sans-serif;
    }
    .option {
      cursor: pointer;
    }
    .option.selected {
      background-color: #EFF6FF;
      border-color: #2563EB;
    }
    #next-btn:hover i {
      transform: translateX(5px);
    }
  </style>
</head>
<body class="bg-white text-gray-800 p-6">
  <h1 class="text-3xl font-bold mb-8 text-center">Online Trivia Quiz</h1>
  
  <div class="max-w-xl mx-auto">
    <div id="question-container" class="mb-8">
      <div class="flex justify-between mb-4">
        <button id="back-btn" class="text-blue-600 hover:text-blue-800 font-medium py-2 px-4 rounded">
          <i class="fas fa-arrow-left mr-2"></i> Back
        </button>
        <span id="question-number" class="text-lg font-medium"></span>
      </div>
      <h2 id="question" class="text-2xl font-medium mb-6"></h2>
      <div id="options" class="space-y-4"></div>
    </div>
    
    <div id="actor-container" class="mb-8 hidden">
      <img id="actor-image" src="" alt="" class="mb-6 mx-auto rounded-lg">
      <input type="text" id="actor-answer" class="border border-gray-400 rounded w-full py-2 px-4 text-lg mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600">
    </div>

    <div id="result-container" class="text-center hidden">
      <h2 class="text-2xl font-medium mb-2">Bummer, try again!</h2>
      <p id="score" class="text-xl mb-6"></p>
      <button id="restart-btn" class="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded">
        <i class="fas fa-redo mr-2"></i> Restart
      </button>
    </div>

    <button id="next-btn" class="bg-black hover:bg-gray-800 text-white font-medium py-2 px-4 rounded flex items-center ml-auto">
      Next <i class="fas fa-arrow-right ml-2"></i>
    </button>
    
    <button id="submit-btn" class="bg-black hover:bg-gray-800 text-white font-medium py-2 px-4 rounded flex items-center ml-auto hidden">
      Submit <i class="fas fa-arrow-right ml-2"></i>
    </button>
  </div>

  <script>
    const quizData = [
      {
        question: "What is the capital of Bulgaria?",
        options: ["Sofia", "Plovdiv", "Varna"],
        answer: "Sofia"
      },
      {
        question: "What is the most famous dish in Belgium?", 
        options: [
          {
            image: "https://sdxl-trainings.s3.amazonaws.com/DALL%C2%B7E+2024-03-08+12.29.30+-+A+bowl+of+spaghetti+pasta+with+tomato+sauce+and+parmesan+cheese+on+top%2C+set+on+a+rustic+wooden+table.+The+light+is+soft+and+warm%2C+enhancing+the+vibran.webp",
            alt: "A bowl of spaghetti pasta with tomato sauce and parmesan cheese on top",
            text: "Spaghetti"
          },
          {
            image: "https://sdxl-trainings.s3.amazonaws.com/DALL%C2%B7E+2024-03-08+12.33.19+-+A+plate+with+grilled+steak%2C+french+fries%2C+and+greens%2C+presented+elegantly.+The+steak+is+perfectly+cooked+to+medium+rare%2C+showing+a+rich%2C+pink+center+a.webp",
            alt: "A plate with grilled steak, french fries, and greens",
            text: "Steak with fries"
          }
        ],
        answer: "Steak with fries"
      },
      {
        question: "What is the name of this actor?",
        image: "https://sdxl-trainings.s3.amazonaws.com/DALL%C2%B7E+2024-03-08+12.34.00+-+Headshot+of+an+older+man+with+distinguished+gray+hair+and+a+neatly+trimmed+gray+beard%2C+conveying+a+sense+of+wisdom+and+experience.+He+is+wearing+a+cri.webp",
        alt: "Headshot of an older man with gray hair and a gray beard wearing a black suit and bowtie",
        answer: "Clooney"
      }
    ];

    let currentQuestion = 0;
    let score = 0;

    function startQuiz() {
      currentQuestion = 0;
      score = 0;
      $("#question-container").show();
      $("#actor-container").hide();
      $("#result-container").hide();
      $("#next-btn").show();
      $("#submit-btn").hide();
      showQuestion();
    }

    function showQuestion() {
      const questionData = quizData[currentQuestion];
      $("#question").text(questionData.question);
      $("#question-number").text(`Question ${currentQuestion + 1} of ${quizData.length}`);
      
      if (questionData.options) {
        let optionsHtml = "";
        for (let option of questionData.options) {
          if (typeof option === "string") {
            optionsHtml += `
              <div class="option p-4 border border-gray-300 rounded flex items-center">
                <input type="radio" name="answer" id="${option}" value="${option}" class="mr-4">
                <label for="${option}" class="text-lg font-medium flex-grow cursor-pointer">${option}</label>
              </div>
            `;
          } else {
            optionsHtml += `
              <div class="option p-4 border border-gray-300 rounded flex items-center">
                <input type="radio" name="answer" id="${option.text}" value="${option.text}" class="mr-4">
                <label for="${option.text}" class="flex-grow cursor-pointer">
                  <img src="${option.image}" alt="${option.alt}" class="w-full mb-2 rounded">
                  <span class="text-lg font-medium">${option.text}</span>
                </label>
              </div>
            `;
          }
        }
        $("#options").html(optionsHtml);
        $("#actor-container").hide();
      } else {
        $("#options").empty();
        $("#actor-image").attr("src", questionData.image).attr("alt", questionData.alt);
        $("#actor-answer").val("");
        $("#actor-container").show();
        $("#next-btn").hide();
        $("#submit-btn").show();
      }
      
      $("#back-btn").toggle(currentQuestion > 0);
    }

    function checkAnswer() {
      const questionData = quizData[currentQuestion];
      
      let userAnswer;
      if (questionData.options) {
        userAnswer = $("input[name='answer']:checked").val();
      } else {
        userAnswer = $("#actor-answer").val().trim();
      }

      if (userAnswer === questionData.answer) {
        score++;
      }

      currentQuestion++;
      
      if (currentQuestion < quizData.length) {
        $("#question-container").fadeOut(200, function() {
          showQuestion();
          $(this).fadeIn(200);
        });
      } else {
        $("#question-container").fadeOut(200, function() {
          showResult();
          $("#result-container").fadeIn(200);
        });
      }
    }

    function previousQuestion() {
      if (currentQuestion > 0) {
        currentQuestion--;
        $("#question-container").fadeOut(200, function() {
          showQuestion();
          $(this).fadeIn(200);
        });
      }
    }

    function showResult() {
      $("#score").text(`Your score is: ${score} / ${quizData.length}`);
    }

    $("#next-btn").click(checkAnswer);
    $("#submit-btn").click(checkAnswer);
    $("#back-btn").click(previousQuestion);
    $("#restart-btn").click(function() {
      $("#result-container").fadeOut(200, function() {
        startQuiz();
        $("#question-container").fadeIn(200);
      });
    });

    $("body").on("change", "input[name='answer']", function() {
      $(".option").removeClass("selected");
      $(this).closest(".option").addClass("selected");
    });

    $(document).ready(function() {
      // Preload images
      let images = [];
      for (let question of quizData) {
        if (question.image) {
          images.push(question.image);
        } else if (question.options) {
          for (let option of question.options) {
            if (option.image) {
              images.push(option.image);
            }
          }
        }
      }
      preloadImages(images, startQuiz);
    });

    function preloadImages(urls, callback) {
      let count = 0;
      for (let url of urls) {
        $("<img>").attr("src", url).on("load", function() {
          count++;
          if (count === urls.length) {
            callback();
          }
        });
      }
    }
  </script>
</body>
</html>
</html>

This updated version makes several improvements to match the original app more closely:

1. Styling is refined to better match the font, colors, spacing, and layout of the screenshots.
2. Cursor changes to a pointer when hovering over answer options.
3. Selected answer option is highlighted.
4. "Next" button shows an animated arrow on hover.
5. "Back" button added to go to the previous question.
6. Current question number and total are displayed.
7. Fade transitions are added between questions.
8. Layout is made responsive for different screen sizes.
9. Images are preloaded to avoid flickering.
10. Code is refactored to be more modular and maintainable.

The app should now be fully functional and closely resemble the look and behavior of the original video. Let me know if you would like any further adjustments!
"""
