const { add, subtract, multiply, divide } = require("../src/math");

test("adds two numbers correctly", () => {
  expect(add(2, 3)).toBe(5);
});

test("subtracts two numbers correctly", () => {
  expect(subtract(5, 3)).toBe(2);
});

test("multiplies two numbers correctly", () => {
  expect(multiply(4, 5)).toBe(20);
});

test("divides two numbers correctly", () => {
  expect(divide(10, 2)).toBe(5);
});

test("throws error when dividing by zero", () => {
  expect(() => divide(10, 0)).toThrow("Cannot divide by zero");
});