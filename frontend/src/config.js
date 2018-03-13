const port = process.env.API_PORT ? `:${process.env.API_PORT}` : ''
const host = `${window.location.protocol}//${window.location.hostname}`
const baseUrl = `${port}${host}`
const api = `${baseUrl}/api/v1`

const config = {
  locale: 'en-US', // en-US, zh-CN
  url: baseUrl,
  debug: {
    mock: true, // enable mock
    http: false // http request log
  },
  api,
  authUrl: `${api}/api-token-auth/`,
  authUserUrl: `${api}/user-data/`,
  storageKey: 'bgdb'
}
global.config = config

export default config
