import type { Metadata, Viewport } from 'next';
import './styles/globals.css';
import './styles/theme.css';
import { Vazirmatn } from 'next/font/google';
import { defaultMetadata } from '@/lib/seo';
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';
import SEOJsonLD from '@/components/SEOJsonLD';

export const metadata: Metadata = defaultMetadata;
export const viewport: Viewport = { themeColor: '#E42217', colorScheme: 'light' };

const vazir = Vazirmatn({ subsets: ['arabic','latin'], variable: '--font-fa', weight: ['400','500','700'], display: 'swap' });

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fa" dir="rtl">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
      </head>
      <body className={vazir.variable}>
        <SEOJsonLD />
        <Navbar />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
