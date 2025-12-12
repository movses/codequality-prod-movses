/* 
* This code is calculatiing the total price
*/

export function processOrder(order) {
  const total = order.price * order.quantity;
  return total;
}
