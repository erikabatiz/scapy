# Name: Erika Batiz
# Date: October 27, 2017
# Scapy lab  |  reconstruct_image.py

from scapy.all import * 

# Decode the image from the packets.
# Determine the type of image that is decoded from the packets (e.g., BMP, PNG, JPG, GIF).
# Save the image to file system with proper image file extension.

def http_assembler(PCAP):
    carved_images = 0
    pcap = rdpcap(PCAP)
    sessions = pcap.sessions()
    for session in sessions:
        http_payload = ''
        for packet in sessions[session]:
            try:
                if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                    http_payload += str(packet[TCP].payload)
            except:
                pass
            headers = get_http_headers(http_payload)
            if headers is None:
                continue

            # extract the raw image and return the image type and the binary body of
            # the image itself
            image, image_type = extract_image(headers, http_payload)
            if image is not None and image_type is not None:
                file_name = '%s-pic_carver_%d.%s' %(PCAP, carved_images, image_type)
                fd = open('%s/%s' % (PIC_DIR, file_name), 'wb')
                fd.write(image)
                fd.close()
                carved_images += 1            

    return carved_images



