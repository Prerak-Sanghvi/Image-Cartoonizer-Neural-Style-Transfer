import torch
from torchvision import transforms, models

def load_nst_model():
    """Load a pre-trained VGG-19 model for style transfer."""
    model = models.vgg19(pretrained=True).features
    for param in model.parameters():
        param.requires_grad = False
    return model

def apply_style_transfer(content_image, style_image, model, steps=500, style_weight=1e6, content_weight=1):
    """Apply style transfer to blend content and style images."""
    # Define transformations
    preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((512, 512)),
        transforms.Lambda(lambda x: x.mul(255))
    ])

    content = preprocess(content_image).unsqueeze(0).requires_grad_(True)
    style = preprocess(style_image).unsqueeze(0)

    # Optimizer
    optimizer = torch.optim.Adam([content], lr=0.01)

    for step in range(steps):
        # Compute losses (skipped here for brevity; use content/style layers from VGG)
        pass

    return content.detach().squeeze().permute(1, 2, 0).byte().numpy()