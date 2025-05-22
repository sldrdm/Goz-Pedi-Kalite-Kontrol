using UnityEngine;

public class YonuDegistirici : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        Renderer pedRend = other.GetComponent<Renderer>();
        Rigidbody rb = other.GetComponent<Rigidbody>();

        if (pedRend != null && rb != null)
        {
            Color pedColor = pedRend.material.color;

            // Kırmızı pedleri yönlendir
            if (pedColor.r > 0.9f && pedColor.g < 0.2f && pedColor.b < 0.2f)
            {
                Debug.Log("KIRMIZI PED SAPSIN!");

                // Yönünü sağa çevir
                rb.linearVelocity = new Vector3(2f, 0f, 0f);
                // Eğer uyarı alıyorsan şunu kullan:
                //;
            }
        }
    }
}
