from supabase import create_client
import os
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)