export function processOrder(order) {
  if (!order) {
    throw new Error("Missing order");          // ← new lines inserted ABOVE
  }

  const total = order.price * order.quantity;  // ← original line moved DOWN
  return total;
}

