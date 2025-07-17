-- Users are managed by Supabase Auth, but we can create profile info here if needed
create table if not exists price_history (
    id uuid default gen_random_uuid() primary key,
    product_id text,
    product_name text,
    brand text,
    supermarket text,
    unit_price numeric,
    quantity text,
    timestamp timestamptz default current_timestamp
);

create table if not exists alerts (
    id uuid default gen_random_uuid() primary key,
    user_id uuid references auth.users(id),
    product_id text,
    threshold_price numeric,
    created_at timestamptz default current_timestamp
);

create table if not exists saved_items (
    id uuid default gen_random_uuid() primary key,
    user_id uuid references auth.users(id),
    product_id text,
    product_name text,
    created_at timestamptz default current_timestamp
);
