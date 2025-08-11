import type { Metadata } from 'next';

export const SITE = {
  name: 'امداد سیف',
  shortName: 'EmdadSafe',
  url: process.env.NEXT_PUBLIC_SITE_URL || 'https://emdadsafe.example.com',
  description:
    'امداد خودرو حرفه‌ای، سریع و ۲۴ ساعته با پوشش شهری و بین‌شهری. یدک‌کش، باتری‌به‌جا، پنچرگیری سیار، سوخت‌رسانی و تعمیر در محل.',
  phone: '+98-21-91300000',
  logo: '/logo.svg',
  locale: 'fa-IR',
};

export const defaultMetadata: Metadata = {
  metadataBase: new URL(SITE.url),
  title: { default: `${SITE.name} | امداد خودرو ۲۴/۷`, template: `%s | ${SITE.name}` },
  description: SITE.description,
  applicationName: SITE.shortName,
  alternates: { canonical: '/' },
  robots: {
    index: true,
    follow: true,
    nocache: false,
    googleBot: { index: true, follow: true, maxSnippet: -1, maxImagePreview: 'large', maxVideoPreview: -1 },
  },
  openGraph: {
    type: 'website',
    siteName: SITE.name,
    title: SITE.name,
    description: SITE.description,
    url: SITE.url,
    images: [{ url: '/og.jpg' }],
    locale: SITE.locale,
  },
  twitter: { card: 'summary_large_image' },
  icons: { icon: '/favicon.ico', shortcut: '/favicon.ico', apple: '/apple-touch-icon.png' },
  category: 'service',
};
