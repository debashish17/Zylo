import { supabase } from '@/lib/supabase'

export async function uploadAsset(
  file: File,
  userId: string,
  assetType: string
): Promise<string> {
  const fileName = `${userId}/${assetType}/${Date.now()}_${file.name}`

  const { data, error } = await supabase.storage
    .from('brand-assets')
    .upload(fileName, file, {
      cacheControl: '3600',
      upsert: false,
    })

  if (error) throw error

  // Get public URL
  const {
    data: { publicUrl },
  } = supabase.storage.from('brand-assets').getPublicUrl(fileName)

  return publicUrl
}

export async function deleteAsset(fileName: string): Promise<void> {
  const { error } = await supabase.storage.from('brand-assets').remove([fileName])

  if (error) throw error
}

export function getOptimizedImageUrl(fileName: string, width: number, height: number): string {
  const { data } = supabase.storage.from('brand-assets').getPublicUrl(fileName, {
    transform: {
      width,
      height,
      resize: 'cover',
    },
  })

  return data.publicUrl
}
