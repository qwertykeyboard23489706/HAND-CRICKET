from pathlib import Path
p=Path('outputs/handcricket.html');s=p.read_text(encoding='utf-8-sig')
old="S.landmarker=await visionApi.HandLandmarker.createFromOptions(vision,{baseOptions:{modelAssetPath:'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task'},runningMode:'VIDEO',numHands:2,minHandDetectionConfidence:.58,minHandPresenceConfidence:.55,minTrackingConfidence:.55});"
new="const modelOptions={baseOptions:{modelAssetPath:'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task'},runningMode:'VIDEO',numHands:2,minHandDetectionConfidence:.58,minHandPresenceConfidence:.55,minTrackingConfidence:.55};try{S.landmarker=await visionApi.HandLandmarker.createFromOptions(vision,{...modelOptions,baseOptions:{...modelOptions.baseOptions,delegate:'GPU'}})}catch(gpuError){console.info('GPU hand tracking unavailable; using CPU',gpuError);S.landmarker=await visionApi.HandLandmarker.createFromOptions(vision,modelOptions)}"
if old not in s: print('landmarker config not found')
else: s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
