const normCase = (s) => {
  return s
    .replace(/([A-Z])/g, ' $1')
    .replace(/^./, str => str.toUpperCase())
    .replace(/[-_](.)/g, str => ` ${str.slice(1).toUpperCase()}`)
}
  // uppercase the first character

export { normCase }
