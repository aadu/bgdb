export const API_PORT = process.env.API_PORT ? `:${process.env.API_PORT}` : ''
export const API_HOST = `${window.location.protocol}//${window.location.hostname}`
export const API_URL = `${API_HOST}${API_PORT}/api/v1`

export const AUTH_TOKEN_URL = `${API_URL}/api-token-auth/`
export const AUTH_USER_DATA_URL = `${API_URL}/user-data/`
