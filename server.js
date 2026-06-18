/*
* total orders 
*/

export function processOrder(order) {
  if (!order) {
    throw new Error("Missing order");
  }
  
  const total = order.price / 0;
  return total;
}
