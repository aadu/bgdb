const port = process.env.API_PORT ? `:${process.env.API_PORT}` : ''
const host = `${window.location.protocol}//${window.location.hostname}`
const baseUrl = `${host}${port}`
const apiUrl = `${baseUrl}/api/v1`

const config = {
  locale: 'en-US', // en-US, zh-CN
  baseUrl: baseUrl,
  debug: {
    mock: true, // enable mock
    http: false // http request log
  },
  apiUrl,
  authUrl: `${baseUrl}/api-token-auth/`,
  registerUrl: `${apiUrl}/users/`,
  gamesUrl: `${apiUrl}/games/`,
  storageKey: 'bgdb'
}
global.config = config

export default config
