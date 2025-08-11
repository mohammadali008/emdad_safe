'use client';
import React from 'react';
import { SITE } from '@/lib/seo';

export default function SEOJsonLD() {
  const org = {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: SITE.name,
    url: SITE.url,
    logo: SITE.logo,
    contactPoint: [{ '@type': 'ContactPoint', telephone: SITE.phone, contactType: 'customer service', areaServed: 'IR' }],
  };

  const business = {
    '@context': 'https://schema.org',
    '@type': 'EmergencyService',
    name: SITE.name,
    url: SITE.url,
    telephone: SITE.phone,
    areaServed: 'IR',
    image: `${SITE.url}/og.jpg`,
    serviceType: ['Roadside assistance','Towing','Battery service','Tire service','Fuel delivery'],
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(org) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(business) }} />
    </>
  );
}
