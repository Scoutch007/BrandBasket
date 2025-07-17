from supabase import create_client, Client

SUPABASE_URL = "https://jbvznqxykfsponlsxafc.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpidnpucXh5a2ZzcG9ubHN4YWZjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI0ODU5MTgsImV4cCI6MjA2ODA2MTkxOH0.aJUMSq-4Et96y2gXgQdSbbSHrQbkaeEgROMr2KkNthw"

def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
