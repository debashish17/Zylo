import fs from 'fs/promises'
import path from 'path'

const UPLOAD_DIR = path.join(process.cwd(), 'uploads')

export async function uploadAsset(
  file: File,
  userId: string,
  assetType: string
): Promise<string> {
  // Create user directory
  const userDir = path.join(UPLOAD_DIR, userId, assetType)
  await fs.mkdir(userDir, { recursive: true })

  // Save file
  const fileName = `${Date.now()}_${file.name}`
  const filePath = path.join(userDir, fileName)
  const buffer = Buffer.from(await file.arrayBuffer())
  await fs.writeFile(filePath, buffer)

  // Return URL
  return `/uploads/${userId}/${assetType}/${fileName}`
}

export async function getAsset(url: string): Promise<Buffer> {
  const filePath = path.join(process.cwd(), url)
  return await fs.readFile(filePath)
}

export async function deleteAsset(url: string): Promise<void> {
  const filePath = path.join(process.cwd(), url)
  await fs.unlink(filePath)
}
