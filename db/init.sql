CREATE TABLE IF NOT EXISTS public.users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

INSERT INTO public.users (name, email)
VALUES ('John Doe', 'john@example.com')
ON CONFLICT (email) DO NOTHING;