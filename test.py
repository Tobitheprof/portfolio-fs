#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://stagnator.openai.azure.com/"
openai.api_version = "2023-09-15-preview"
openai.api_key = "b7d481e88bb940dc871956251fc509b2"

response = openai.Completion.create(
  engine="cont-gen-app",
  prompt="Generate a multiple choice quiz from the text below. Quiz should contain at least 5 questions. Each answer choice should be on a separate line, with a blank line separating each question.\n\nA neutron star is the collapsed core of a massive supergiant star, which had a total mass of between 10 and 25 solar masses, possibly more if the star was especially metal-rich. Neutron stars are the smallest and densest stellar objects, excluding black holes and hypothetical white holes, quark stars, and strange stars. Neutron stars have a radius on the order of 10 kilometers (6.2 mi) and a mass of about 1.4 solar masses. They result from the supernova explosion of a massive star, combined with gravitational collapse, that compresses the core past white dwarf star density to that of atomic nuclei.\n\nExample:\nQ1. What is a neutron star?\nA. The collapsed core of a massive supergiant star\nB. The smallest and densest stellar object\nC. A white hole\nD. A quark star",
  temperature=0.8,
  max_tokens=500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.5,
  stop=None)

print(response)