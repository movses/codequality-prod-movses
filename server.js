/*
*  This code is calculating total price
*/

export function processOrder(order) {
  const total = order.price * order.quantity;
  return total;
}
