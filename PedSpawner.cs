using UnityEngine;

public class PedSpawner : MonoBehaviour
{
    public GameObject pedPrefab;
    public float spawnInterval = 2f;
    public Vector3 spawnPosition = new Vector3(0, 0.55f, 0);

    public Material matSaglam;
    public Material matHatali;

    private float timer = 0f;

    void Update()
    {
        timer += Time.deltaTime;
        if (timer >= spawnInterval)
        {
            GameObject newPed = Instantiate(pedPrefab, spawnPosition, Quaternion.identity);

            // %30 olasılıkla hatalı yap
            bool hataliMi = Random.value < 0.3f;

            Renderer rend = newPed.GetComponent<Renderer>();
            if (rend != null)
            {
                rend.material = hataliMi ? matHatali : matSaglam;
            }

            // 🎯 EKLEDİĞİMİZ SATIR:
            Destroy(newPed, 4f); // 5 saniye sonra otomatik silinir

            timer = 0f;
        }
    }
}
