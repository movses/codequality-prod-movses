export function processOrder(order) {
  const total = order.price * order.quantity;   // ← reviewer comments here
  return total;
}
