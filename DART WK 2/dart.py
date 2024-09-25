// Function to calculate the total price with an optional tax parameter
double calculateTotal(List<double> prices, {double tax = 0}) {
  double total = prices.fold(0, (sum, price) => sum + price);
  total += total * tax;  // Apply tax if provided
  return total;
}

// Function to apply a discount using a higher-order function
List<double> applyDiscount(List<double> prices, double Function(double) discountFunction) {
  return prices.map((price) => discountFunction(price)).toList();
}

// Recursive function to calculate a factorial-based discount percentage
int calculateFactorialDiscount(int n) {
  if (n <= 1) return 1;
  return n * calculateFactorialDiscount(n - 1);
}

void main() {
  // Sample item prices in the shopping cart
  List<double> itemPrices = [12.99, 49.99, 5.49, 25.00, 8.99, 15.99];

  // Anonymous function to filter out items below a certain threshold (e.g., items under $10)
  List<double> filteredPrices = itemPrices.where((price) => price >= 10).toList();
  print('Filtered Prices: $filteredPrices');

  // Discount function reducing price by a percentage (e.g., 10%)
  double discountPercentage = 10;
  double discountFunction(double price) => price * (1 - (discountPercentage / 100));

  // Apply the discount to all items in the cart
  List<double> discountedPrices = applyDiscount(filteredPrices, discountFunction);
  print('Discounted Prices: $discountedPrices');

  // Calculate the total price with tax (e.g., 5%)
  double taxRate = 0.05;
  double totalPriceWithTax = calculateTotal(discountedPrices, tax: taxRate);
  print('Total Price with Tax: \$${totalPriceWithTax.toStringAsFixed(2)}');

  // Special discount based on the factorial of the number of items in the cart
  int numberOfItems = discountedPrices.length;
  int factorialDiscountPercent = calculateFactorialDiscount(numberOfItems);
  print('Factorial Discount Percent: $factorialDiscountPercent%');

  // Apply the factorial-based discount to the final total price
  double finalPrice = totalPriceWithTax * (1 - (factorialDiscountPercent / 100));
  print('Final Price after Factorial Discount: \$${finalPrice.toStringAsFixed(2)}');
}