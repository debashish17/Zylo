'use client'

import { useEffect, useRef, useState } from 'react'
import { fabric } from 'fabric'

interface CreativeCanvasProps {
  format: 'SQUARE_1_1' | 'PORTRAIT_4_5' | 'STORIES_9_16'
  onCanvasChange?: (canvas: fabric.Canvas) => void
}

const FORMAT_DIMENSIONS = {
  SQUARE_1_1: { width: 1080, height: 1080 },
  PORTRAIT_4_5: { width: 1080, height: 1350 },
  STORIES_9_16: { width: 1080, height: 1920 },
}

export function CreativeCanvas({ format, onCanvasChange }: CreativeCanvasProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const fabricCanvasRef = useRef<fabric.Canvas | null>(null)
  const [isReady, setIsReady] = useState(false)

  useEffect(() => {
    if (!canvasRef.current) return

    // Initialize Fabric.js canvas
    const dimensions = FORMAT_DIMENSIONS[format]
    const canvas = new fabric.Canvas(canvasRef.current, {
      width: dimensions.width,
      height: dimensions.height,
      backgroundColor: '#ffffff',
    })

    fabricCanvasRef.current = canvas

    // Add sample text for testing
    const text = new fabric.IText('Click to edit', {
      left: dimensions.width / 2,
      top: dimensions.height / 2,
      fontSize: 48,
      fill: '#000000',
      originX: 'center',
      originY: 'center',
    })
    canvas.add(text)

    setIsReady(true)

    // Canvas change event
    canvas.on('object:modified', () => {
      onCanvasChange?.(canvas)
    })

    return () => {
      canvas.dispose()
    }
  }, [format, onCanvasChange])

  return (
    <div className="relative border rounded-lg overflow-hidden bg-gray-100 flex items-center justify-center">
      <canvas ref={canvasRef} />
      {!isReady && (
        <div className="absolute inset-0 flex items-center justify-center">
          <div className="text-muted-foreground">Loading canvas...</div>
        </div>
      )}
    </div>
  )
}
