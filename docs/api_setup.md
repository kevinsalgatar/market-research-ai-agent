# API Setup Guide

## Required API Keys

### OpenAI API Key
1. Visit https://platform.openai.com
2. Sign up or log in
3. Go to API keys section
4. Create a new API key

### Brave Search API Key
1. Visit https://brave.com/search/api/
2. Sign up for Brave Search API
3. Create a new API key
4. Free tier includes:
   - 2,000 searches/month
   - Web, news, and local search
   - Full API access

### Browserless API Key (Optional)
1. Visit https://browserless.io
2. Sign up for an account
3. Get your API key
4. Used for advanced web scraping

## Configuration

1. Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```

2. Edit the `.env` file with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
BRAVE_API_KEY=your_brave_api_key_here
BROWERLESS_API_KEY=your_browserless_api_key_here
```

## Usage Notes

### Brave Search API
- Rate limits: 2,000 searches/month on free tier
- Includes web, news, and local search
- No credit card required
- Higher tiers available for more volume

### Error Handling
The search tools will automatically handle:
- Rate limiting
- API errors
- Invalid responses

If you encounter any issues:
1. Check your API key is correct
2. Verify you haven't exceeded rate limits
3. Check the API status at https://brave.com/search/api/status