import { type MetadataRoute } from 'next';
import { SITE } from '@/lib/seo';

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    { url: `${SITE.url}/`, changeFrequency: 'weekly', priority: 1 },
    { url: `${SITE.url}/services`, changeFrequency: 'weekly', priority: 0.9 },
    { url: `${SITE.url}/blog`, changeFrequency: 'weekly', priority: 0.6 },
    { url: `${SITE.url}/faq`, changeFrequency: 'monthly', priority: 0.5 },
    { url: `${SITE.url}/contact`, changeFrequency: 'monthly', priority: 0.5 },
  ];
}
