export function processOrder(order) {
  if (!order) {
    throw new Error("Missing order");
  }

  if (!order.price) {
    throw new Error("Missing price");
  }

  const total = order.price / 0;
  return total;
}

