export function processOrder(order) {
  const total = order.price * order.quantity;
  return total;
}
