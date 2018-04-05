const normCase = (s) => {
  return s
    .replace(/([A-Z])/g, ' $1')
    .replace(/^./, str => str.toUpperCase())
}
  // uppercase the first character

export { normCase }
