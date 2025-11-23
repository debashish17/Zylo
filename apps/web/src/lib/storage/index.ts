// Storage adapter - switches between local and Supabase based on environment
import * as localStorage from './local'
import * as supabaseStorage from './supabase'

const IS_PRODUCTION = process.env.NODE_ENV === 'production'

// Automatically use local storage in development, Supabase in production
export const storage = IS_PRODUCTION ? supabaseStorage : localStorage
